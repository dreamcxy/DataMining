function peg()
    D1training = load('dataset1-a8a-training.txt');
    [n11,d11] = size( D1training);
    D1testing = load('dataset1-a8a-testing.txt');
    [n12,d12] = size( D1testing);
    D2training = load('dataset1-a9a-training.txt');
    [n21,d21] = size(D2training);
    D2testing = load('dataset1-a9a-testing.txt');
    [n22,d22] = size(D2testing);
    
    X1 = D1training(:, 1:d11-1);
    y1 = D1training(:, d11);
    X2 = D2training(:, 1:d21-1);
    y2 = D2training(:, d21);
    
    X1Test = D1testing(:, 1:d12-1);
    y1Test = D1testing(:, d12);
    X2Test = D2testing(:, 1:d22-1);
    y2Test = D2testing(:, d22);
    
    lamda_1 = 10^(-4);
    lamda_2 = 5 * 10^(-5);
    m1 = n11;
    m2 = n21;
    T1 = 5 * m1;
    T2 = 5 * m2;
    %进行10次循环
    errorRate = zeros(4, 10);
    coe = 0.1;
    k = 1;
    coeScale = k * coe;
    while coeScale <= 1.0
            % training on dataset1---hinge loss
            w11 = zeros(1, d11-1);%行向量
            t1 = 1;
            while t1 <= coeScale * T1
                i_t1 = fix(n11 * rand(1) + 1);%从1~n11之间随机均匀取一个数
                eta_1 = 1 / (lamda_1 * t1);
                temp1 = y1( i_t1) * (w11 * X1( i_t1,:)');
                if  temp1 < 1
                    w11 = (1 - eta_1 * lamda_1) * w11 + eta_1 * y1( i_t1) * X1( i_t1, :);
                else
                    w11 = (1-eta_1*lamda_1) * w11;
                end
                w11 = min( 1,1/( sqrt(lamda_1)*norm(w11) ) ) * w11;
                 t1 = t1 + 1;
            end
            % training on dataset2---hinge loss
            w12 = zeros(1, d21 - 1);%行向量
            t2 = 1;
            while t2 <= coeScale * T2
                i_t2 = fix(n21*rand(1) + 1);%从1~n21之间随机均匀取一个数
                eta_2 = 1 / (lamda_2 * t2);
                temp2 = y2( i_t2) * (w12 * X2( i_t2, :)');
                if  temp2 < 1
                    w12 = (1 - eta_2 * lamda_2) * w12 + eta_2 * y2( i_t2) * X2( i_t2, :);
                else
                    w12 = (1 - eta_2 * lamda_2) * w12;
                end
                w12 = min(1, 1 / (sqrt(lamda_2) * norm(w12) ) ) * w12;
                 t2 = t2 + 1;
            end
            
            % training on dataset1----logit loss
            w21 = zeros(1, d11-1);%行向量
            t1 = 1;
            while t1 <= coeScale * T1
                i_t1 = fix(n11*rand(1) + 1);%从1~n11之间随机均匀取一个数
                eta_1 = 1 / (lamda_1 * t1);
                w21 = (1 - eta_1 * lamda_1) * w21 + (y1(i_t1) / (1 + exp(y1(i_t1) * (w21 * X1( i_t1, :)')))) * X1( i_t1, :);
                w21 = min(1, 1 / (sqrt(lamda_1) * norm(w21) ) ) * w21;
                t1 = t1 + 1;
            end
            
            % training on dataset2----logit loss
            w22 = zeros(1, d21 - 1);%行向量
            t2 = 1;
            while t2 <= coeScale * T2
                i_t2 = fix(n21 * rand(1) + 1);%从1~n21之间随机均匀取一个数
                eta_2 = 1/(lamda_2 * t2);
                w22 = (1- eta_2 * lamda_2) * w22 + (y2(i_t2) / (1 + exp(y2(i_t2) * (w22 * X2( i_t2, :)')))) * X2( i_t2, :);
                w22 = min( 1, 1 / ( sqrt(lamda_2) * norm(w22) ) ) * w22;
                t2 = t2 + 1;
            end

            %testing on dataset1---hinge loss
            t1 = 1;
            errorCnt1 = 0;
            while  t1 <= n12
                if((w11 * X1Test(t1, :)') * y1Test(t1) < 0)
                    errorCnt1 = errorCnt1 + 1;
                end
                t1 = t1 + 1;
            end
            errorRate(1, k) = roundn(errorCnt1 / n12, -3);
            fprintf('coeScale is %1.1f :\n', coeScale);
            fprintf('testing1-Hinge loss:   error rate is:%1.3f\n', errorRate(1, k));
            
            %testing on dataset2---hinge loss
            t2 = 1;
            errorCnt2 = 0;
            while  t2 <= n22
                if((w12*X2Test(t2, :)')*y2Test(t2) < 0)
                    errorCnt2 = errorCnt2 + 1;
                end
                t2 = t2 + 1;
            end
            errorRate(2,k) = roundn(errorCnt2 / n22, -3);
            fprintf('testing2-Hinge loss:    error rate is:%1.3f\n', errorRate(2, k));

            
            
            %testing on dataset1----logit loss
            t1 = 1;
            errorCnt1 = 0;
            while  t1 <= n12
                if((w21*X1Test(t1, :)') * y1Test(t1) < 0)
                    errorCnt1 = errorCnt1 + 1;
                end
                t1 = t1 + 1;
            end
            errorRate(3,k) = roundn(errorCnt1 / n12, -3);
            fprintf('testing1-Logit loss:    error rate is:%1.3f\n',errorRate(3,k));
            
            %testing on dataset2----logit loss
            t2 = 1;
            errorCnt2 = 0;
            while  t2 <= n22
                if((w22 * X2Test(t2, :)') * y2Test(t2) < 0)
                    errorCnt2 = errorCnt2 + 1;
                end
                t2 = t2 + 1;
            end
            errorRate(4,k) = roundn(errorCnt2 / n22, -3);
            fprintf('testing2-Logit loss:    error rate is:%1.3f\n', errorRate(4,k));
           
            k = k + 1;
            coeScale = k * coe;
    end
end

