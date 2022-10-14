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
      // url  'https://meicerto.com.br/checkout-2/?add-to-cart=836&quantity='+qt;
      
      //<button type="submit" name="wpforms[submit]" id="wpforms-submit-519" class="wpforms-submit redireciona" data-alt-text="Enviando..." data-submit-text="Enviar" aria-live="assertive" value="wpforms-submit">Enviar</button>
  });

  $('#wpforms-submit-1668').on('click', function(event) {
    event.preventDefault(); 
    var url = $(this).data('https://meicerto.com.br/checkout-2/?add-to-cart=836&quantity='+qt);
    //location.replace(url);
    alert(location.replace(url));
});

  });
  
  </script>