function solution(A,B){
    var answer = 0;
    A.sort((a,b) => a-b);
    B.sort((c,d) => d-c);
    for (i = 0 ; i <A.length ; i++){
        answer += A[i]*B[i];
    }
    
    return answer;
}