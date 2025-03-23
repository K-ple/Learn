#반복문
for(i in 1:3){
    print(i)
}

data <- c('a', 'b', 'c')
for(i in data){
    print(i)
}

i <- 0
while(i < 5){
    i <- i + 1
    print(i)
}

#조건문
number <- 5
if (number < 5){
    print('5보다 작다')
} else if (number == 5){
    print('5와 같다')
} else {
    print('5보다 크다')
}

number <- 3
if (number < 5){
    print('5보다 작다')
} else if (number == 5){
    print('5와 같다')
} else {
    print('5보다 크다')
}

number <- 7
if (number < 5){
    print('5보다 작다')
} else if (number == 5){
    print('5와 같다')
} else {
    print('5보다 크다')
}
print('')

#사용자 정의 함수
comparedTo5 <- function(x) {
    if (x < 5){
        print('5보다 작다')
    } else if (x == 5){
        print('5와 같다')
    } else {
        print('5보다 크다')
    }
}

comparedTo5(10)
comparedTo5(3)
comparedTo5(5)

