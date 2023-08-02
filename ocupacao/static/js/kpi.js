window.onload = () =>{
    mediaOcupacoes();
};

const tbody = document.querySelector("tbody");
const mediaOcupacoes = () =>{
    if(tbody){
        const QntOcupacoes = tbody.children.length;
        let media = 0;
        for (let i = 0; i < QntOcupacoes; i++) {
            const tr = tbody.children[i];
            let tdOcupacao = tr.lastElementChild;

            if(tdOcupacao.innerText.length == 4)
                tdOcupacao = Number(tdOcupacao.innerText.slice(0,3));
            else tdOcupacao = Number(tdOcupacao.innerText.slice(0,2));
        
            media += tdOcupacao;
        }
        media /= QntOcupacoes;
        montarTrMedia(media);
    }
};

const montarTrMedia = media => {
    const HTML = `<tr>
        <td style="border: 1px solid rgb(168, 168, 168);" class="bg-light">
        X
        </td>
        <td style="border: 1px solid rgb(168, 168, 168);" class="bg-light">
        X
        </td>
        <td style="border: 1px solid rgb(168, 168, 168);" class="bg-light">
        X
        </td>
        <td style="border: 1px solid rgb(168, 168, 168);" class="bg-light">
        X
        </td>
        <td style="border: 1px solid rgb(168, 168, 168);" class="bg-light">
        X
        </td>
        <td style="border: 1px solid rgb(168, 168, 168);" class="bg-light">
        ${media}%
        </td>
    <tr>`
    tbody.innerHTML += HTML;
}