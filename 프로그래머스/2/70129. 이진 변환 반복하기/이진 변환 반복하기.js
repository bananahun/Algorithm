function solution(s) {
    let chkZero = ''
    let cntZero = 0
    let sumZero = 0
    let cntTrans = 0
    let result = ''
    
    do {
        chkZero = s.match(/0/g)
        if (chkZero !=null){
            cntZero = chkZero.length
            sumZero += cntZero
        }
        let delZeroLength = s.replaceAll('0','').length
        result = delZeroLength.toString(2)
        s = result
        cntTrans++
    } while (s != 1)
        
    return [cntTrans, sumZero]
}