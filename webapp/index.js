// Modify this url if necessary !!!
const flaskUrl = 'http://localhost:5000';

function underline2CamelCase(str){
    const words = str.split('_');
    let camelCaseWord = '';

    for(const word of words){
        if(camelCaseWord.length > 0)
            camelCaseWord += ' ';
        camelCaseWord += word.charAt(0).toUpperCase() + word.slice(1);
    }

    return camelCaseWord;
}

async function getGameData(rank) {
    const response = await fetch('https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=' + rank);
    const rankData = await response.json();

    // Attach image url to each member
    for(const game of rankData.data){
        game.image_url = 'images/' + game.civilization + '.png';
        // Transform civilization name to camel case
        game.formattedCivName = underline2CamelCase(game.civilization);
    }

    return rankData;
}

async function getSchema() {
    const schema = await fetch('/sample.json');
    return await schema.json();
}

async function handleWinRateFetching(rank, refresh) {
    const response = await fetch(flaskUrl + `/api/solodata/rank/winrate?rank=${rank}&refresh=${refresh}`);
    const spec = await response.json();

    vegaEmbed('#views', spec);
}

async function handleGameCountFetching(rank, refresh) {
    const response = await fetch(flaskUrl + `/api/solodata/rank/games_count?rank=${rank}&refresh=${refresh}`);
    const spec = await response.json();

    vegaEmbed('#views2', spec);
}

// Deprecated after using flask as backend
async function handleDataFetching(rank) {
    console.log(rank);
    const [spec, gameData] = await Promise.all([getSchema(), getGameData(rank)]);

    spec.data = {
        name: "AOE4-Data",
        values: gameData.data
    };

    if(rank === '≥conqueror_4')
        spec.title.subtitle = 'In Top'
    else    // 首字母转大写
        spec.title.subtitle = 'In Rank ' + rank.charAt(0).toUpperCase() + rank.slice(1);

    vegaEmbed('#views', spec);
}

// handleDataFetching('overall')
handleWinRateFetching('overall', 'no');
handleGameCountFetching('overall', 'no');