$(document).ready(function (){
  cadastrar_receita();
  addIngredientesParaReceita();
});




function cadastrar_receita(){
  $('#nova-receita').submit(function (e){
    var formData = new FormData($(this)[0]);
    var url = "../main/nova_receita";
    $.ajax({
      type: 'POST',
      url: url,
      data: formData,
      async: true,
      success: function (data) {
        console.log(data);
        displayData(data);
      },
      contentType: false,
      cache: false,
      processData: false
    });
    e.preventDefault();
  });
}

function addIngredientesParaReceita(){
  $('#ingredientes').submit(function (e){

    let data = {};
    let form = this;

    data['id_receita'] = $('#id-receita').val();
    data['id_ingrediente'] = $('#id_ingrediente').val();
    data['porcentagem'] = $('#porcentagem').val();
    console.log(data);

    var url = "../main/ingrediente_receita";


    $.ajax({
      type: 'POST',
      url: url,
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify(data),
      success: function (data){

      },
    });
    e.preventDefault();
  })
}

function displayData(response){
    var idReceita = response.id_receita;

    $.each(response.ingredientes, function(k, ingrediente){
      var option = document.createElement("option");
      $(option).attr("value", ingrediente.id);
      $(option).html(ingrediente.nome);
      $("#id_ingrediente").append(option);
    });


    $("#id-receita").attr("value", idReceita);
    $("#ingredientes").css("display", "block");
}
