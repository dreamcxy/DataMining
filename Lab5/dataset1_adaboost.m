DEGREE = [0, 1]';
TRAINLENGTH = length(dataset1.feature1);
proOfDegree = zeros(1, length(DEGREE));
maxFeature1 = max(dataset1.feature1);
maxFeature2 = max(dataset1.feature2);
maxFeature3 = max(dataset1.feature3);
maxFeature4 = max(dataset1.feature4);
maxFeature5 = max(dataset1.feature5);
maxFeature6 = max(dataset1.feature6);
maxFeature7 = max(dataset1.feature7);
maxFeature8 = max(dataset1.feature8);
maxFeature9 = max(dataset1.feature9);
 
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
        if dataset1.label(j) == DEGREE(i)
            countLabel  = countLabel + 1; 
        end
    end
    proOfDegree(i) = countLabel;
end

for i = 1:maxFeature1
    for j = 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature1(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature1(i,k) = countFeature1(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature2
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature2(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature2(i,k) = countFeature2(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature3
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature3(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature3(i,k) = countFeature3(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature4
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature4(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature4(i,k) = countFeature4(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature5
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature5(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature5(i,k) = countFeature5(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature6
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature6(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature6(i,k) = countFeature6(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature7
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature7(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature7(i,k) = countFeature7(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature8
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature8(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature8(i,k) = countFeature8(i,k) + 1;
            end
        end
    end
end
for i = 1:maxFeature9
    for j= 1:TRAINLENGTH
        for k = 1:length(DEGREE)
            if dataset1.feature9(j) == i && dataset1.label(j) == DEGREE(k)
                countFeature9(i,k) = countFeature9(i,k) + 1;
            end
        end
    end
end

TESTLENGTH = length(dataset1.feature1);
bayesDegree = zeros(TESTLENGTH, 1);
features = zeros(TESTLENGTH, 9);
countError = 0;
countSame = zeros(TESTLENGTH, 1);
literations = 6;
weight = ones(literations, TESTLENGTH)/TESTLENGTH;
alpha = zeros(literations, 1);
count = zeros(literations, TESTLENGTH);
for m = 1:literations - 1
    
    for i  = 1:TESTLENGTH
        features(i,1) = dataset1.feature1(i);
        features(i,2) = dataset1.feature2(i);
        features(i,3) = dataset1.feature3(i);
        features(i,4) = dataset1.feature4(i);
        features(i,5) = dataset1.feature5(i);
        features(i,6) = dataset1.feature6(i);
        features(i,7) = dataset1.feature7(i);
        features(i,8) = dataset1.feature8(i);
        features(i,9) = dataset1.feature9(i);
        pro = zeros(length(DEGREE), 9);
        for j = 1:TRAINLENGTH
            for k = 1:length(DEGREE)
                if dataset1.label(j) == DEGREE(k) && dataset1.feature1(j) == features(i,1)
                    pro(k,1) = pro(k,1) + 1;
                end
                if dataset1.label(j) == DEGREE(k) && dataset1.feature2(j) == features(i,2)
                    pro(k,2) = pro(k,2) + 1;
                end
                if dataset1.label(j) == DEGREE(k) && dataset1.feature3(j) == features(i,3)
                    pro(k,3) = pro(k,3) + 1;
                end
                 if dataset1.label(j) == DEGREE(k) && dataset1.feature4(j) == features(i,4)
                    pro(k,4) = pro(k,4) + 1;
                 end
                 if dataset1.label(j) == DEGREE(k) && dataset1.feature5(j) == features(i,5)
                    pro(k,5) = pro(k,5) + 1;
                 end
                 if dataset1.label(j) == DEGREE(k) && dataset1.feature6(j) == features(i,6)
                    pro(k,6) = pro(k,6) + 1;
                 end
                 if dataset1.label(j) == DEGREE(k) && dataset1.feature4(7) == features(i,7)
                    pro(k,7) = pro(k,7) + 1;
                 end
                 if dataset1.label(j) == DEGREE(k) && dataset1.feature8(j) == features(i,8)
                    pro(k,8) = pro(k,8) + 1;
                 end
                 if dataset1.label(j) == DEGREE(k) && dataset1.feature9(j) == features(i,9)
                    pro(k,9) = pro(k,9) + 1;
                 end
            end
            if dataset1.feature1(j) == features(i,1) && dataset1.feature2(j) == features(i,2) && dataset1.feature3(j) == features(i,3)...
                    && dataset1.feature4(j) == features(i,4) && dataset1.feature5(j) == features(i,5) && dataset1.feature6(j) == features(i,6) ...
                    && dataset1.feature7(j) == features(i,7) && dataset1.feature8(j) == features(i,8) && dataset1.feature9(j) == features(i,9)
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
        if bayesDegree(i) ~= dataset1.label(i)
            countError = (countError + 1) * weight(m, i);    
        end
        alpha(m,1) = log(double((1-countError)/countError));
        if bayesDegree(i) == dataset1.label(i)
            weight(m+1, i) = weight(m, i)*exp(-alpha(m, 1));
        else
            weight(m+1, i) = weight(m, i)*exp(alpha(m, 1));
        end
        weight(m+1, i) = weight(m+1, i)/sum(weight(m+1, i));
        count(m, i) = count(m, i) + alpha(m, 1)*bayesDegree(i);
    end
end
sign(count)














 





