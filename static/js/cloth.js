$(document).ready(function () {
    $(".add-cart-btn").click(function () {
        let brand = $("#clothBrand").text()
        let code = $('input[name="cloth_code"]').val()
        let clothSize = []

        clothSize.push($('input[name="XS"]:checked').val())
        clothSize.push($('input[name="S"]:checked').val())
        clothSize.push($('input[name="L"]:checked').val())
        clothSize.push($('input[name="XL"]:checked').val())
        clothSize.push($('input[name="XXL"]:checked').val())
        let price = $('input[name="price"]').val()
        let shippingCost = $('input[name="shipping_cost"]').val()
        let image = $('input[name="cloth_img"]').val()
        let pieces = $('input[name="pieces"]').val()
        let color = $('input[name="color"]').val()

        let addedClothes = clothSize
            .filter(s => s !== undefined)
            .map(s => {
                let clothes = JSON.parse(localStorage.getItem('clothes'))
                if (clothes !== null) {
                    let cloth = {
                        code,
                        brand,
                        size: s,
                        pieces,
                        price,
                        shippingCost,
                        image,
                        color
                    }
                    clothes.push(cloth)
                    localStorage.setItem('clothes', JSON.stringify(clothes))
                } else {
                    let cloth = [{
                        code,
                        brand,
                        size: s,
                        pieces,
                        price,
                        shippingCost,
                        image,
                        color
                    }]
                    localStorage.setItem('clothes', JSON.stringify(cloth))
                }
            })

        if (addedClothes.length > 0) {
            $("#errorMessage").remove()
            calculateTotalCost()
            setTimeout(() => location.reload(), 1000)
        } else {
            $("#addErrorMessage").append(`<p class="mt-3" id="errorMessage">The details are not filled correctly...</p>`)
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
