literations = 6;
accuracy = zeros(10 ,1);
for i = 1:10
    if i == 1
        testset = dataset2(2:101, 1:25);
        trainset = dataset2(102:1001, 1:25);
    else
        testset = dataset2(100*i-98:100*i+1, 1:25);
        trainset = [dataset2(2:100*i-99, 1:25);dataset2(100*i+2:1001, 1:25)];
    end
    trainlength = length(trainset.feature1);
    testlength = length(testset.feature1);
    weight = ones(literations, testlength)/testlength;
    alpha = zeros(literations, 1);
    apsl = zeros(literations, 1);
    mthbayesdegree = zeros(testlength, 1);
    for m = 1: literations - 1
        bayesdegree = dataset2_bayes(trainset, testset, [1,-1]');
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
