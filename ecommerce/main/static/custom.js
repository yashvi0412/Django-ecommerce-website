$(document).ready(function(){
    $(".choose-size").hide();
   // show size according to selected color
    $(".choose-color").on('click',function(){
        $(".choose-color").removeClass('focused');
        $(this).addClass('focused');

        var _color=$(this).attr('data-color');

        $(".choose-size").hide();
        $(".color"+_color).show();
        $(".color"+_color).first().addClass('active');

        var _price=$(".color"+_color).first().attr('data-price');
        $(".product-price").text(_price);

    });
 
    //show the price acc to selected size
    $(".choose-size").on('click',function(){
        $(".choose-size").removeClass('active');
        $(this).addClass('active');

        var _price=$(this).attr('data-price');
        $(".product-price").text(_price);
    });
 
    $(".choose-color").first().addClass('focused'); 
    var _color=$(".choose-color").first().attr('data-color');
    var _price=$(".choose-size").first().attr('data-price');

    $(".color"+_color).show();
    $(".color"+_color).first().addClass('active');
    $(".product-price").text(_price);

    //add to cart
    $(document).on('click',"#addToCartBtn",function(){
        var _vm=$(this);
        var _qty =$("#productQty").val();
        var _productId =$(".product-id").val();
        var _productTitle =$(".product-title").val();
       // console.log(_qty, -_productId, _productTitle);
        var _productPrice =$(".product-price").text();
        
        $.ajax({
            url:'/add-to-cart',
			data:{
                'id':_productId,
                'qty': _qty,
                'title':_productTitle,
                'price':_productPrice
                  
            },
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
        })

    });
});