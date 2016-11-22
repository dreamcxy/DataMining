function grade = judgegrade( data )
%     switch data
%         case data>=0 && data<0.25 
%             grade = 1;
%         case data>=0.25 && data<0.5
%             grade = 2;
%         case data>=0.5 && data<0.75
%             grade = 3;
%         case data>=0.75 && data<=1
%             grade = 4;
%     end
    if data >= 0 && data < 0.25
        grade = 1;
    else if data < 0.5
            grade = 2;
        else if data < 0.75
                grade = 3;
            else if data <= 1
                    grade =4;
                end
            end
        end
    end
    
end

