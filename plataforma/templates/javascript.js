<script type = "text/javascript" >

  let qt;
  var $jq = jQuery.noConflict()
  
  $jq(document).ready(function() {
  
  //Quando o campo cep perde o foco.
  $jq("#wpforms-519-field_43").change(function() {
  
      //Nova variável "cep" somente com dígitos.
      var valores = $jq(this).val();
      let quantidade =parseInt(valores.length);
      qt = quantidade;
      
      console.log('https://meicerto.com.br/checkout-2/?add-to-cart=1677&quantity='+qt);

     

     
  });

  $jq("#wpforms-submit-519").click(function() {
  
    location.href = 'https://meicerto.com.br/checkout-2/?add-to-cart=836&quantity='+qt;

   

   
});
  
  });
  
  </script>


