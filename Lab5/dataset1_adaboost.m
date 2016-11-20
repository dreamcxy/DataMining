DEGREE = [0, 1]';
TRAINLENGTH = length(dataset1train.feature1);
proOfDegree = zeros(1, length(DEGREE));
maxFeature1 = max(dataset1train.feature1);
maxFeature2 = max(dataset1train.feature2);
maxFeature3 = max(dataset1train.feature3);
maxFeature4 = max(dataset1train.feature4);
maxFeature5 = max(dataset1train.feature5);
maxFeature6 = max(dataset1train.feature6);
maxFeature7 = max(dataset1train.feature7);
maxFeature8 = max(dataset1train.feature8);
maxFeature9 = max(dataset1train.feature9);
 
countFeature1 = zeros(maxFeature1, length(DEGREE));
countFeature2 = zeros(maxFeature2, length(DEGREE));
countFeature3 = zeros(maxFeature3, length(DEGREE));
countFeature4 = zeros(maxFeature4, length(DEGREE));
countFeature5 = zeros(maxFeature5, length(DEGREE));
countFeature6 = zeros(maxFeature6, length(DEGREE));
countFeature7 = zeros(maxFeature7, length(DEGREE));
countFeature8 = zeros(maxFeature8, length(DEGREE));
countFeature9 = zeros(maxFeature9, length(DEGREE));

for i = 1:length(proOfDegree)
    countLabel = 0;
    for j = 1: TRAINLENGTH
        if dataset1train.label(j) == DEGREE(i)
            countLabel  = countLabel + 1; 
        end
    end
    proOfDegree(i) = countLabel;
end

for i = 1:maxFeature1
    for j = 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature1(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature1(i,k) = countFeature1(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature2
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature2(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature2(i,k) = countFeature2(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature3
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature3(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature3(i,k) = countFeature3(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature4
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature4(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature4(i,k) = countFeature4(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature5
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature5(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature5(i,k) = countFeature5(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature6
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature6(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature6(i,k) = countFeature6(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature7
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature7(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature7(i,k) = countFeature7(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature8
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature8(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature8(i,k) = countFeature8(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature9
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.feature9(j) == i && dataset1train.label(j) == DEGREE(k)
                countFeature9(i,k) = countFeature9(i,k) + 1;
            end
        end
    end
end

TESTLENGTH = length(dataset1test.feature1);
bayesDegree = zeros(TESTLENGTH, 1);
features = zeros(TESTLENGTH, 9);
countError = 0;
countSame = zeros(TESTLENGTH, 1);
for i  = 1:TESTLENGTH
    features(i,1) = dataset1test.feature1(i);
    features(i,2) = dataset1test.feature2(i);
    features(i,3) = dataset1test.feature3(i);
    features(i,4) = dataset1test.feature4(i);
    features(i,5) = dataset1test.feature5(i);
    features(i,6) = dataset1test.feature6(i);
    features(i,7) = dataset1test.feature7(i);
    features(i,8) = dataset1test.feature8(i);
    features(i,9) = dataset1test.feature9(i);
    pro = zeros(length(DEGREE), 9);
    for j = 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1train.label(j) == DEGREE(k) && dataset1train.feature1(j) == features(i,1)
                pro(k,1) = pro(k,1) + 1;
            end
            if dataset1train.label(j) == DEGREE(k) && dataset1train.feature2(j) == features(i,2)
                pro(k,2) = pro(k,2) + 1;
            end
            if dataset1train.label(j) == DEGREE(k) && dataset1train.feature3(j) == features(i,3)
                pro(k,3) = pro(k,3) + 1;
            end
             if dataset1train.label(j) == DEGREE(k) && dataset1train.feature4(j) == features(i,4)
                pro(k,4) = pro(k,4) + 1;
             end
             if dataset1train.label(j) == DEGREE(k) && dataset1train.feature5(j) == features(i,5)
                pro(k,5) = pro(k,5) + 1;
             end
             if dataset1train.label(j) == DEGREE(k) && dataset1train.feature6(j) == features(i,6)
                pro(k,6) = pro(k,6) + 1;
             end
             if dataset1train.label(j) == DEGREE(k) && dataset1train.feature4(7) == features(i,7)
                pro(k,7) = pro(k,7) + 1;
             end
             if dataset1train.label(j) == DEGREE(k) && dataset1train.feature8(j) == features(i,8)
                pro(k,8) = pro(k,8) + 1;
             end
             if dataset1train.label(j) == DEGREE(k) && dataset1train.feature9(j) == features(i,9)
                pro(k,9) = pro(k,9) + 1;
             end
        end
        if dataset1train.feature1(j) == features(i,1) && dataset1train.feature2(j) == features(i,2) && dataset1train.feature3(j) == features(i,3)...
                && dataset1train.feature4(j) == features(i,4) && dataset1train.feature5(j) == features(i,5) && dataset1train.feature6(j) == features(i,6) ...
                && dataset1train.feature7(j) == features(i,7) && dataset1train.feature8(j) == features(i,8) && dataset1train.feature9(j) == features(i,9)
            countSame(i) = countSame(i) + 1;
        end
        
    end
    guessProbability = zeros(length(DEGREE), 1);
    probability = prod(pro);
    for k = 1:length(DEGREE)
        guessProbability(k) = double((probability(k))/(countSame(i)*proOfDegree(k)^8));
    end
    [degreeProbability, degreePosition] = max(guessProbability);
    bayesDegree(i) = DEGREE(degreePosition);
    if bayesDegree(i) ~= dataset1test.label(i)
        countError = countError + 1;    
    end
end
double(countError/TESTLENGTH)





















