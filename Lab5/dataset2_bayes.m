function bayesdegree = dataset2_bayes(trainset, testset, DEGREE)
trainlength = length(trainset.VarName1)
proofdegree = zeros(1, length(degree));
countError = 0;
countFeature13 = zeros(max(trainset.feature13), length(DEGREE));
countFeature14 = zeros(max(trainset.feature14), length(DEGREE));
countFeature15 = zeros(max(trainset.feature15), length(DEGREE));
countFeature16 = zeros(max(trainset.feature16), length(DEGREE));
countFeature17 = zeros(max(trainset.feature17), length(DEGREE));
countFeature18 = zeros(max(trainset.feature18), length(DEGREE));
countFeature19 = zeros(max(trainset.feature19), length(DEGREE));
countFeature20 = zeros(max(trainset.feature20), length(DEGREE));
countFeature21 = zeros(max(trainset.feature21), length(DEGREE));
countFeature22 = zeros(max(trainset.feature22), length(DEGREE));
countFeature23 = zeros(max(trainset.feature23), length(DEGREE));
countFeature24 = zeros(max(trainset.feature24), length(DEGREE));
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
for i = 1: max(trainset.feature13)
    for j = 1:trainlength
        for k = 1:length(DEGREE)
            if trainset.feature13(j) == i && trainset.label(j) == DEGREE(j)
                countFeature13(i, k) = countFeature13(i, k) + 1;
            end
        end
    end
end



end

