function solution(s){
    let check = 0;
    const arr = s.split('');
    if (arr[0] === ')'){
        return false
    }
    for (i = 0 ; i <arr.length ; i++){
        if (arr[i] === '('){
            check += 1
        }
        else {check -= 1
             if (check < 0) return false}
        
    }
    return check === 0 ? true : false
}