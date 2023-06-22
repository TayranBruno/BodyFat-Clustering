document.getElementById('cluster-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var weight = parseFloat(document.getElementById('weight').value);
    var height = parseFloat(document.getElementById('height').value);
    var chest = parseFloat(document.getElementById('chest').value);
    var abdomen = parseFloat(document.getElementById('abdomen').value);
    var age = parseInt(document.getElementById('age').value);
  
    var data = {
      'Weight': weight,
      'Height': height,
      'Chest': chest,
      'Abdomen': abdomen,
      'Age': age
    };
  
    fetch('http://localhost:5000/clusterizar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(function(response) {
      return response.text();
    })
    .then(function(result) {
      var jsonResult = JSON.parse(result);
      document.getElementById('result').textContent = 'Cluster: ' + jsonResult.cluster;
    })
    .catch(function(error) {
      console.log('Error:', error);
    });
});
