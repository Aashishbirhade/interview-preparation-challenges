function ispalindrome(a){
    b = a
    rev = 0
    while (a>0){
        rem = a%10
        rev = rev*10 + rem
        a = Math.round(a/10)   
    }
    if(rev == b){
        return "is palindrome"
    }
    return "none"
}
let a = 121
console.log(ispalindrome(a))