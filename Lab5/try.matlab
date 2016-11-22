for i = 1: grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature1(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature1(i,k) = countFeature1(i,k) + 1;
                end
            end
        end
    end
    for i = 1: grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature2(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature2(i,k) = countFeature2(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
            for k = 1: length(DEGREE)
                if judgegrade(trainset.feature3(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature3(i,k) = countFeature3(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
           for k = 1:length(DEGREE)
               if judgegrade(trainset.feature4(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature4(i,k) = countFeature4(i,k) + 1;
               end
           end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature5(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature5(i,k) = countFeature5(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1: trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature6(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature6(i,k) = countFeature6(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature7(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature7(i,k) = countFeature7(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j= 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature8(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature8(i,k) = countFeature8(i,k) + 1;
                end
            end
        end
    end
    for i= 1:grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature9(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature9(i,k) = countFeature9(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature10(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature10(i,k) = countFeature10(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature11(j)) == i && trainset.label(j) == DEGREE(k)
                    countFeature11(i,k) = countFeature11(i,k) + 1;
                end
            end
        end
    end
    for i = 1:grade
        for j = 1:trainlength
            for k = 1:length(DEGREE)
                if judgegrade(trainset.feature12(j)) == i && trainset.label(j) == DEGREE(k) 
                    countFeature12(i,k) = countFeature12(i,k) + 1;
                end
            end
        end
    end


if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature1(j)) == judgegrade(features(i,1))
                    pro(k,1) = pro(k,1) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature2(j)) == judgegrade(features(i,2))
                    pro(k,2) = pro(k,2) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature3(j)) == judgegrade(features(i,3))
                    pro(k,3) = pro(k,3) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature4(j)) == judgegrade(features(i,4))
                    pro(k,4) = pro(k,4) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature5(j)) == judgegrade(features(i,5))
                    pro(k,5) = pro(k,5) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature6(j)) == judgegrade(features(i,6))
                    pro(k,6) = pro(k,6) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature7(j)) == judgegrade(features(i,7))
                    pro(k,7) = pro(k,7) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature8(j)) == judgegrade(features(i,8))
                    pro(k,8) = pro(k,8) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature9(j)) == judgegrade(features(i,9))
                    pro(k,9) = pro(k,9) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature10(j)) == judgegrade(features(i,10))
                    pro(k,10) = pro(k,10) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature11(j)) == judgegrade(features(i,11))
                    pro(k,11) = pro(k,11) + 1;
                end
                if trainset.label(j) == DEGREE(k) && judgegrade(trainset.feature12(j)) == judgegrade(features(i,12))
                    pro(k,12) = pro(k,12) + 1;
                end




    judgegrade(trainset.feature1(j)) == judgegrade(features(i,1)) && judgegrade(trainset.feature2(j)) == judgegrade(features(i,2)) ...
                    && judgegrade(trainset.feature3(j)) == judgegrade(features(i,3)) && judgegrade(trainset.feature4(j)) == judgegrade(features(i,4))...
                    && judgegrade(trainset.feature5(j)) == judgegrade(features(i,5)) && judgegrade(trainset.feature6(j)) == judgegrade(features(i,6))...
                    && judgegrade(trainset.feature7(j)) == judgegrade(features(i,7)) && judgegrade(trainset.feature8(j)) == judgegrade(features(i,8))...
                    && judgegrade(trainset.feature9(j)) == judgegrade(features(i,9)) && judgegrade(trainset.feature10(j)) == judgegrade(features(i,10))...
                    && judgegrade(trainset.feature11(j)) == judgegrade(features(i,11)) && judgegrade(trainset.feature12(j)) == judgegrade(features(i,12))...