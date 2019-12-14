clear all;
close all;
clc;

tic
AF = [];

% Vale edw onomata fakelwn me lekseis isou mege8ous
sp1 = 'spea1';            
sp2 = 'spea2';
sp3 = 'spea3';
sp4 = 'spea4';
sp5 = 'spea5';

allf = [sp1; sp2; sp3; sp4; sp5];

oldpath = cd;    

for sp = 1 : size(allf,1)    
  
    cd(allf(sp,:))              
    files = dir(strcat('test','/*.wav'));    
  
    for i = 1:length(files)
        [audio{i}, fs] = audioread(files(i).name);
        a = miraudio(audio{i},fs);      
        win = 0.04;      
        over = 0.5;      
        AF_new = win_overlap(a,win,over,sp);   
        if i==1
            AF = AF_new;
        else
            AF = [AF; AF_new];
        end      
    end
    
    if sp==1
          AF_sum= AF;
    else
          AF_sum = [AF_sum; AF];
    end
    
    cd(oldpath)

end

str = sprintf('Vouli'); % Apo8hkeuse edw onoma pinaka pou 8a bgalei
save(str, 'AF_sum')

toc