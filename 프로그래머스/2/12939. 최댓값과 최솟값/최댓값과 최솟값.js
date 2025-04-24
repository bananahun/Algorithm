function solution(s) {
    const arr = s.split(' ');
    console.log(arr)
    return Math.min(...arr) + ' ' + Math.max(...arr);
}