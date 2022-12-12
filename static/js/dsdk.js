

function tdStt(){
    let a = document.querySelectorAll('.tdSTT')
    let b = 0
    for(i = 1; i<=a.length;i++){
        a[b].textContent = i
        b++
    }   
}
tdStt()