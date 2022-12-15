// $(window).on("scroll", function () {
//     $(this).scrollTop() > 650 ? $(".product-category").addClass("category-fixed") : $(".product-category").removeClass("category-fixed");
// }),
    // $(".action-cart").on("click", function () {
    //     var c = $(this).parents(".product-action-group").children();
    //     c.first().css("display", "none"), c.last().css("display", "flex");
    // }),
    // $(".action-wish").on("click", function () {
    //     $(this).toggleClass("active");
    // }),
    $(".column-4").on("click", function () {
        $(".column-4 i").css({ color: "var(--white)", background: "var(--primary)" }),
            $(".column-3 i").css({ color: "var(--primary)", background: "var(--primary-light)" }),
            $(".action-cart").addClass("active"),
            $(".product-part").find(".col-xl-4").addClass("col-xl-3"),
            $(".product-part").find(".col-xl-4").removeClass("col-xl-4"),
            $(".column-3").on("click", function () {
                $(".column-3 i").css({ color: "var(--white)", background: "var(--primary)" }),
                    $(".column-4 i").css({ color: "var(--primary)", background: "var(--primary-light)" }),
                    $(".action-cart").removeClass("active"),
                    $(".product-part").find(".col-xl-3").addClass("col-xl-4"),
                    $(".product-part").find(".col-xl-3").removeClass("col-xl-3");
            });
    });
