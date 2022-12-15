$(".voucher-btn").on("click", function () {
    $(this).hide(), $(".check-footer").css("margin-top", "0px"), $(".voucher-form").css("display", "flex");
}),
    $(".load-btn .btn").click(function () {
        $(this).append('<span class="spinner-border spinner-border-sm"></span>');
    }),
    $(".contact").on("click", function () {
        $(".contact").removeClass("active"), $(this).addClass("active");
    }),
    $(".address").on("click", function () {
        $(".address").removeClass("active"), $(this).addClass("active");
    }),
    $(".payment").on("click", function () {
        $(".payment").removeClass("active"), $(this).addClass("active");
    });

// document.addEventListener("contextmenu", (e) => e.preventDefault()),
//     (document.onkeydown = function (e) {
//         return 123 == e.keyCode ? (alert("F12 Disable"), !1) : e.ctrlKey && 67 == e.keyCode ? (alert("ctrl + c disable"), !1) : e.ctrlKey && 85 == e.keyCode ? (alert("ctrl + u disable"), !1) : void 0;
//     });
