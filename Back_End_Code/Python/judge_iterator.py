class TimeIterator:
    
    def __init__(self,start, stop) -> None:
        self.start_hour = start//3600
        self.start_minute = (start%3600)//60
        self.start_second = start%60     
        if self.start_hour > 23:
            self.start_hour = 0
        #if self.stop_hour > 23:
            #self.stop_hour = 0
        self.start = start
        self.stop = stop
        self.tlist = []


    def __iter__ (self):
        return self
    
    def __next__(self):        
        
        if self.start < self.stop:    
            tr = (':'.join([str(self.start_hour).zfill(2),str(self.start_minute).zfill(2),str(self.start_second).zfill(2)]))      
            self.tlist.append
            self.start_second += 1
            if self.start_second == 60:
                self.start_second = 0
                self.start_minute += 1
            if self.start_minute == 60:
                self.start_minute = 0
                self.start_hour += 1
        else:
            raise StopIteration
        self.start += 1
        return tr      
        
            
            
        
            
            

    def __getitem__(self, index):
        if 0 <= index <= self.stop - self.start:
            hour = self.start_hour + index // 3600
            minute = self.start_minute + (index % 3600) // 60
            second = self.start_second + index % 60
            return '{}:{}:{}'.format(str(hour).zfill(2),str(minute).zfill(2),str(second).zfill(2))
        else:
            raise IndexError

    
                    
start, stop, index = map(int,input().split())
for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')