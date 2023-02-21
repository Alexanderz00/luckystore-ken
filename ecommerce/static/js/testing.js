var updateBtns = document.getElementsByClassName('update-cart')

// button is HTMLButtonElement class

// console.log('typeof this:', this.constructor)
// console.log('typeof this.dataset:', typeof this.dataset)

// var productId = this.dataset.product

console.log('*** adding listener 02')

for(var i=0; i < updateBtns.length; i++){
	console.log('*** adding listener 2222')
    updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    console.log('USER:', 'user 99', productId, type(updateBtns[i]))
    })
}

if (updateBtns.length > 0){
    var button = updateBtns[0]
    console.log('button.constructor:', button.constructor)
    console.log('button.name:', button.name)
    console.log('button.type:', button.type)
    console.log('button.value:', button.value)
    console.log('button.labels:', button.labels)
    console.log('button.labels.length:', button.labels.length)
    let className = button.getAttribute('class')
    console.log('className:', className)
    console.log('button.className:', button.className)
}else{
    console.log('No button can be found')
}
