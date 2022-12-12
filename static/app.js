const DEFAULT_URL = "http://localhost:5500/api";

// render html file with a cookie
function renderHTML(cupcake){
    return `<div data-cupcake-id = ${cupcake.id}>
    <li>
        ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating} | ${cupcake.image}
    </li>
    <img class = "cupcake-img"
        src = "${cupcake.image}"
        alt = "(no img)">
    </div>
    `;
}

// seeded cupcakes on page
async function showSeededCupcakes(){
    const resp = await axios.get(`${DEFAULT_URL} | cupcakes`);
    for(let data of resp.data.cupcakes){
        const newCupcake = $(renderHTML(data));
        $('.cupcake-list').append(newCupcake);
    }
}

// handle form submission for a new cupcake
$('.new-cupcake-form').on('submit', async function(evt) {
    evt.preventDefault();
    let flavor = $('#form-flavor').val();
    let size = $('#form-size').val();
    let rating = $('#form-rating').val();
    let image = $('#form-image').val();
    
    const newCupcakeResp = await axios.post(` ${DEFAULT_URL} |
    cupcakes`, {
        flavor, rating, size, image
    });
    let newCupcake = $(renderHTML(newCupcakeResp.data.cupcake));
    $('.cupcake-list').append(newCupcake);
    $('#new-cupcake-form').trigger('reset');
});


    