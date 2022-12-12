
function lapDSKham(id, nameNB, gioiTinh, namSinh, ngayDKKham, address){
    fetch("/ds-kham",{
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'name': nameNB,
            'gioiTinh': gioiTinh,
            'namSinh': namSinh,
            'ngayDKKham': ngayDKKham,
            'address': address
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res) {
        console.info(res)
        return res.json()
    }).then(function(data) {
        console.info(data)
    })
    let test = document.querySelector('.duyet'+id)
    test.remove()
}

//Thêm và xóa dòng thuốc
    // $('#myTable > tbody:last-child').append('<tr>...</tr><tr>...</tr>');
function addRow(){
    let parent = document.querySelector('.tbody')
    let addTr = document.createElement('tr')
    parent.appendChild(addTr)
    let i
    for(i = 1; i<=4; i++){
        let addTd = document.createElement('td')
        let addInput = document.createElement('input')
        addTd.classList = 'setPhieuKham' 
        addInput.type = 'text'
        addInput.name = 'name' + i
        addTr.appendChild(addTd)
        addTd.appendChild(addInput)
    } 
}
function total(){
    let tienKham = parseFloat(document.getElementById('tienKham').value)
    let tienThuoc = parseFloat(document.getElementById('tienThuoc').value)
    // console.log(Number(tienKham))
    // console.log(parseFloat(tienKham))
    let tongTien = document.getElementById('tongTien')
    let sum =0
    sum = tienKham + tienThuoc
    tongTien.value = sum.toFixed(3)
}

