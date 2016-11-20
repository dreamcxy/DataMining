a = [1,2,3,4];
for i = 1: 4
    a(:, i) = a(:, i)/norm(a(:,i));
end
a