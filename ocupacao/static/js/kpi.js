window.onload = () =>{
    if(corpoTabela)
        mediaOcupacoes();
};

const corpoTabela = document.querySelector("tbody");
const QntOcupacoes = corpoTabela.children.length;

const mediaOcupacoes = () =>{
    let media = 0;
    for (let i = 0; i < QntOcupacoes; i++) {
        const tr = corpoTabela.children[i];
        let tdOcupacao = tr.lastElementChild;

        if(tdOcupacao.innerText.length == 4)
            tdOcupacao = Number(tdOcupacao.innerText.slice(0,3));
        else tdOcupacao = Number(tdOcupacao.innerText.slice(0,2));
    
        media += tdOcupacao;
    }
    media /= QntOcupacoes;
    montarTrMedia(media);
};

const montarTrMedia = media => {
    const tr = document.createElement("tr");
    for (let i = 0; i < 6; i++) {
        const td = document.createElement("td");
        td.style.border = "1px solid rgb(168, 168, 168)";
        i == 5 ? td.innerText = `${media}%` : td.innerText = "X";
        tr.appendChild(td);
    }
    corpoTabela.appendChild(tr);
}