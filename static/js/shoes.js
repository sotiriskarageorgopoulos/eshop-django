$(document).ready(function () {
    let initial_size = $('input[name="slider-size"]').val()
    $("#size").val(initial_size)

    $('input[name="slider-size"]').change(function () {
        let newSize = $(this).val()
        $("#size").val(newSize)
    })
})