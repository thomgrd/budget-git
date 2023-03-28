$(document).ready(function() {
    $('#budget-form').submit(function(event) {
      event.preventDefault(); // Empêcher la soumission normale du formulaire
      var amount = $('#budget-amount').val(); // Récupérer le montant du budget entré par l'utilisateur
      $.ajax({
        url: '/budgets',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ amount: amount }),
        success: function(response) {
          alert('Budget ajouté avec succès!'); // Afficher une notification de succès
          $('#budget-amount').val(''); // Vider le champ de saisie
        },
        error: function(xhr, status, error) {
          console.log(xhr.responseText); // Afficher l'erreur dans la console
          alert('Une erreur est survenue lors de l\'ajout du budget.'); // Afficher une notification d'erreur
        }
      });
    });
  });
  