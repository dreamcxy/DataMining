literations = 3;
accuracy = zeros(10 ,1);
for i = 1:10
    if i == 1
        testset = dataset1(1:27, 1:10);
        trainset = dataset1(28:270, 1:10);
    else
        testset = dataset1(27*i-26:27*i, 1:10);
        trainset = [dataset1(1:27*i-27, 1:10);dataset1(27*i+1:270, 1:10)];
    end
    trainlength = length(trainset.feature1);
    testlength = length(testset.feature1);
    weight = ones(literations, testlength)/testlength;
    alpha = zeros(literations, 1);
    apsl = zeros(literations, 1);
    mthbayesdegree = zeros(testlength, 1);
    for m = 1: literations - 1
        bayesdegree = bayes(trainset, testset, [0,1]');
        for j = 1: testlength
            if bayesdegree(j) ~= testset.label(j)
                apsl(m,1) = apsl(m,1) + weight(m, j) * abs(bayesdegree(j) - testset.label(j));
            end
        end
        alpha(m, 1) = log((1 - apsl(m, 1))/apsl(m,1));
        for j = 1: testlength
            if bayesdegree(j) == testset.label(j)
                weight(m+1, j) = weight(m, j)*exp(-alpha(m, 1));
            else
                weight(m+1, j) = weight(m, j)*exp(alpha(m, 1));
            end
        end
        weight(m+1, :) = weight(m+1, :)/sum(weight(m+1,:));
        mthbayesdegree = mthbayesdegree + alpha(m, 1)*bayesdegree;
    end
    Mbayesdegree = sign(mthbayesdegree);
    for j = 1: testlength
        if Mbayesdegree(j) == testset.label(j)
            accuracy(i, 1) = accuracy(i, 1) + 1;
        end
    end
    accuracy(i,1) = double(accuracy(i,1)/testlength);
end
accuracy