function bayesdegree = dataset2_bayes(trainset, testset, DEGREE)
    trainlength = length(trainset.feature1);
    proofdegree = zeros(1, length(DEGREE));
    countError = 0;
    
    grade = 4;
    countFeature1 = zeros(grade, length(DEGREE));
    countFeature2 = zeros(grade, length(DEGREE));
    countFeature3 = zeros(grade, length(DEGREE));
    countFeature4 = zeros(grade, length(DEGREE));
    countFeature5 = zeros(grade, length(DEGREE));
    countFeature6 = zeros(grade, length(DEGREE));
    countFeature7 = zeros(grade, length(DEGREE));
    countFeature8 = zeros(grade, length(DEGREE));
    countFeature9 = zeros(grade, length(DEGREE));
    countFeature10 = zeros(grade, length(DEGREE));
    countFeature11 = zeros(grade, length(DEGREE));
    countFeature12 = zeros(grade, length(DEGREE));
    countFeature13 = zeros(max(trainset.feature13)-min(trainset.feature13)+1, length(DEGREE));
    countFeature14 = zeros(max(trainset.feature14)-min(trainset.feature14)+1, length(DEGREE));
    countFeature15 = zeros(max(trainset.feature15)-min(trainset.feature15)+1, length(DEGREE));
    countFeature16 = zeros(max(trainset.feature16)-min(trainset.feature16)+1, length(DEGREE));
    countFeature17 = zeros(max(trainset.feature17)-min(trainset.feature17)+1, length(DEGREE));
    countFeature18 = zeros(max(trainset.feature18)-min(trainset.feature18)+1, length(DEGREE));
    countFeature19 = zeros(max(trainset.feature19)-min(trainset.feature19)+1, length(DEGREE));
    countFeature20 = zeros(max(trainset.feature20)-min(trainset.feature20)+1, length(DEGREE));
    countFeature21 = zeros(max(trainset.feature21)-min(trainset.feature21)+1, length(DEGREE));
    countFeature22 = zeros(max(trainset.feature22)-min(trainset.feature22)+1, length(DEGREE));
    countFeature23 = zeros(max(trainset.feature23)-min(trainset.feature23)+1, length(DEGREE));
    countFeature24 = zeros(max(trainset.feature24)-min(trainset.feature24)+1, length(DEGREE));
    % 1?12 0 && 13:24 1
    for i = 1:length(proofdegree)
        countlabel = 0;
        for j = 1: trainlength
            if trainset.label(j) == DEGREE(i)
                countlabel = countlabel + 1;
            end
            proofdegree(i) = countlabel;
        end
    end
    for i = 1:max(trainset.feature1)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature1(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature1(i,k) = countFeature1(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature1)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature1(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature1(i,k) = countFeature1(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature2)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature2(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature2(i,k) = countFeature2(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature3)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature3(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature3(i,k) = countFeature3(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature4)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature4(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature4(i,k) = countFeature4(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature5)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature5(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature5(i,k) = countFeature5(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature6)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature6(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature6(i,k) = countFeature6(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature7)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature7(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature7(i,k) = countFeature7(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature8)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature8(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature8(i,k) = countFeature8(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature9)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature9(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature9(i,k) = countFeature9(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature10)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature10(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature10(i,k) = countFeature10(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature11)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature11(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature11(i,k) = countFeature11(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature12)
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if trainset.feature12(j) == i && trainset.label(j) == DEGREE(k)
                    countFeature12(i,k) = countFeature12(i,k) + 1;
                end
            end
        end
    end
    
    
    
    for i = 1: max(trainset.feature13)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature13(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature13(i, k) = countFeature13(i, k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature14)
        for j = 1: trainlength
            for k = 1: length(DEGREE)
                if trainset.feature14(j) ==i-1 && trainset.label(j) == DEGREE(k)
                    countFeature14(i, k) = countFeature14(i, k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature15)
        for j = 1 : trainlength
            for k = 1:length(DEGREE)
                if trainset.feature15(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature15(i,k) = countFeature15(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature16)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature16(j) ==i-1  && trainset.label(j) == DEGREE(k)
                    countFeature16(i,k) = countFeature16(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature17)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature17(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature17(i,k) = countFeature17(i,k) + 1;
                end
            end
        end
    end
    for i = 1: max(trainset.feature18)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature18(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature18(i,k) = countFeature18(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature19)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature19(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature19(i,k) = countFeature19(i,k) + 1;
                end
            end
     
        end
    end
    for i = 1:max(trainset.feature20)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature20(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature20(i,k) = countFeature20(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature21)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature21(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature21(i,k) = countFeature21(i,k) + 1;
                end
            end
        end
    end
    for i = 1:max(trainset.feature22)
        for j = 1:trainlength
            for k = 1 : length(DEGREE)
                if trainset.feature22(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature22(i,k) = countFeature22(i,k) + 1;
                end
            end
        end
    end
    for i = 1: max(trainset.feature23)
       for j=  1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature23(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature23(i,k) = countFeature23(i,k) + 1;
                end
            end
       end
    end
    for i = 1 :max(trainset.feature24)
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if trainset.feature24(j) == i-1 && trainset.label(j) == DEGREE(k)
                    countFeature24(i,k) = countFeature24(i,k) + 1;
                end
            end
        end
    end
    
    featurenumber = 24;
    testlength = length(testset.feature1);
    bayesdegree = zeros(testlength, 1);
    features = zeros(testlength, featurenumber);
    countsame = zeros(testlength, 1);
    for i = 1: testlength
        features(i,1) = testset.feature1(i);
        features(i,2) = testset.feature2(i);
        features(i,3) = testset.feature3(i);
        features(i,4) = testset.feature4(i);
        features(i,5) = testset.feature5(i);
        features(i,6) = testset.feature6(i);
        features(i,7) = testset.feature7(i);
        features(i,8) = testset.feature8(i);
        features(i,9) = testset.feature9(i);
        features(i,10) = testset.feature10(i);
        features(i,11) = testset.feature11(i);
        features(i,12) = testset.feature12(i);
        features(i,13) = testset.feature13(i);
        features(i,14) = testset.feature14(i);
        features(i,15) = testset.feature15(i);
        features(i,16) = testset.feature16(i);
        features(i,17) = testset.feature17(i);
        features(i,18) = testset.feature18(i);
        features(i,19) = testset.feature19(i);
        features(i,20) = testset.feature20(i);
        features(i,21) = testset.feature21(i);
        features(i,22) = testset.feature22(i);
        features(i,23) = testset.feature23(i);
        features(i,24) = testset.feature24(i);
        
        pro = zeros(length(DEGREE), featurenumber);
        for j = 1: trainlength
            for k = 1: length(DEGREE)
                if trainset.label(j) == DEGREE(k) && trainset.feature1(j) == features(i,1)
                    pro(k,1) = pro(k,1) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature2(j) == features(i,2)
                    pro(k,2) = pro(k,2) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature3(j) == features(i,3)
                    pro(k,3) = pro(k,3) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature4(j) == features(i,4)
                    pro(k,4) = pro(k,4) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature5(j) == features(i,5)
                    pro(k,5) = pro(k,5) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature6(j) == features(i,6)
                    pro(k,6) = pro(k,6) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature7(j) == features(i,7)
                    pro(k,7) = pro(k,7) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature8(j) == features(i,8)
                    pro(k,8) = pro(k,8) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature9(j) == features(i,9)
                    pro(k,9) = pro(k,9) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature10(j) == features(i,10)
                    pro(k,10) = pro(k,10) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature11(j) == features(i,11)
                    pro(k,11) = pro(k,11) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature12(j) == features(i,12)
                    pro(k,12) = pro(k,12) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature13(j) == features(i,13)
                    pro(k,13) = pro(k,13) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature14(j) == features(i,14)
                    pro(k,14) = pro(k,14) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature15(j) == features(i,15)
                    pro(k,15) = pro(k,15) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature16(j) == features(i,16)
                    pro(k,16) = pro(k,16) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature17(j) == features(i,17)
                    pro(k,17) = pro(k,17) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature18(j) == features(i,18)
                    pro(k,18) = pro(k,18) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature19(j) == features(i,19);
                    pro(k,19) = pro(k,19) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature20(j) == features(i,20)
                    pro(k,20) = pro(k,20) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature21(j) == features(i,21)
                    pro(k,21) = pro(k,21) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature22(j) == features(i,22)
                    pro(k,22) = pro(k,22) + 1;
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature23(j) == features(i,23)
                    pro(k,23) = pro(k,23) + 1; 
                end
                if trainset.label(j) == DEGREE(k) && trainset.feature24(j) == features(i,24)
                    pro(k,24) = pro(k,24) + 1;
                end
            end
                if trainset.feature1(j) == features(i,1) && trainset.feature2(j) == features(i,2) && trainset.feature3(j) == features(i,3)...
                    && trainset.feature4(j) == features(i,4) && trainset.feature5(j) == features(i,5) && trainset.feature6(j) == features(i,6)...
                    && trainset.feature7(j) == features(i,7) && trainset.feature8(j) == features(i,8) && trainset.feature9(j) == features(i,9)...
                    && trainset.feature10(j) == features(i,10) && trainset.feature11(j) == features(i,11) && trainset.feature12(j) == features(i,12)...
                    && trainset.feature13(j) == features(i,13) && trainset.feature14(j) == features(i,14) && trainset.feature15(j) == features(i,15)...
                    && trainset.feature16(j) == features(i,16) && trainset.feature17(j) == features(i,17) && trainset.feature18(j) == features(i,18)...
                    && trainset.feature19(j) == features(i,19) && trainset.feature20(j) == features(i,20) && trainset.feature21(j) == features(i,21)...
                    && trainset.feature22(j) == features(i,22) && trainset.feature23(j) == features(i,23) && trainset.feature24(j) == features(i,24)
                countsame(i) = countsame(i) + 1;
                end
        end  
        guessprobability = zeros(length(DEGREE), 1);
        probability = prod(pro);
        for k = 1:length(DEGREE)
            guessprobability(k) = double((probability(k))/(countsame(i)*proofdegree(k)^23));
        end
        [~, degreeposititon] = max(guessprobability);
        bayesdegree(i) = DEGREE(degreeposititon);
        if bayesdegree(i) ~= testset.label(i)
            countError = countError + 1;
        end
    end
    
    
end











