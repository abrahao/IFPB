<?php

// Verifica se o estado foi enviado via POST
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['estado'])) {
    $codigoDoEstado = $_POST['estado']; // Obtém o código do estado

    // Função para fazer a requisição à API do IBGE
    function obterCidadesPorEstado($codigoDoEstado) {
        $url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/$codigoDoEstado/municipios";
        $ch = curl_init($url);

        // Configuração das opções da requisição
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        // Faz a requisição e obtém a resposta
        $response = curl_exec($ch);

        // Fecha a conexão
        curl_close($ch);

        // Decodifica a resposta JSON
        $cities = json_decode($response, true);

        return $cities;
    }

    // Obtém as cidades do estado especificado
    $cities = obterCidadesPorEstado($codigoDoEstado);

    // Verifica se houve erro na requisição
    if (isset($cities['erro'])) {
        echo "Erro ao obter cidades do estado $codigoDoEstado: " . $cities['erro'];
    } else {
        // Exibe as cidades
        echo "<h2>Cidades do estado de $codigoDoEstado:</h2>";
        echo "<ul>";
        foreach ($cities as $city) {
            echo "<li>" . $city['nome'] . "</li>";
        }
        echo "</ul>";
    }
} else {
    echo "Nenhum estado selecionado";
}
?>
