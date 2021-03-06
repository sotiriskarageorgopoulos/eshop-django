$(document).ready(function () {
    $(".add-cart-btn").click(function () {
        let brand = $("#shoeBrand").text()
        let code = $('input[name="shoe_code"]').val()
        let size = $('input[name="size_number"]:checked').val()
        let color = $('input[name="color"]').val()
        let shippingCost = $('input[name="shipping_cost"]').val()
        let price = $('input[name="price"]').val()
        let image = $('input[name="image"').val()

        let shoeObj = {brand,code,size,color,shippingCost,price,image}
        let clothes = JSON.parse(localStorage.getItem('clothes'))

        if(isValidSize()) {
            if(clothes !== null) {
                clothes.push(shoeObj)
                localStorage.setItem('clothes',JSON.stringify(clothes))
            }
            else {
                localStorage.setItem('clothes',JSON.stringify([shoeObj]))
            }
            calculateTotalCost()
            setTimeout(() => location.reload(), 1000)
        }
        else {
            shoeObj = {}
            $("#addErrorMessage").append(`<p class="mt-3" id="errorMessage">The size is not chosen...</p>`)
        }

        function isValidSize() {
            return size !== "" && size !== null && size !== undefined
        }
    })
})

function calculateTotalCost() {
    let clothes = JSON.parse(localStorage.getItem('clothes'))
    let totalCost = 0
    let realCost = 0
    let shippingCost = 0
    clothes.map(c => {
        if(c.pieces !== undefined) {
            realCost += Number(c.pieces) * Number(c.price)
            shippingCost = Number(c.shippingCost)
        }
        else {
            realCost += Number(c.price)
            shippingCost = Number(c.shippingCost)
        }
    })

    if(realCost > 50) {
        totalCost = realCost
        shippingCost = 0
    }
    else {
        totalCost = realCost + shippingCost
    }

    localStorage.setItem('totalCost', totalCost)
    localStorage.setItem('shippingCost', shippingCost)
}