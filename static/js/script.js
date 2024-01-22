/* Create lists for cascading dropdowns */
let filterObject = {
    "# Pieces": ["<500", "<1000", ">500", ">1000", ">2500", ">5000"],
    "Build Status": ["Build Next", "New", "Stored", "Wish List"],
    "Missing Pieces": ["Yes", "No"],
    "Favourite": ["Yes", "No"]
};
window.onload = function() {
    /* Locate cascading filter elements */
    let filterSel = document.getElementById("set-filter");
    let subFilter = document.getElementById("sub-filter");
    /* Set the options for the initial filter dropdown */
    for (let filter in filterObject) {
        filterSel.options[filterSel.options.length] = new Option(filter, filter);
    }
    /* When the initial dropdown selection is done ... */
    filterSel.onchange = function() {
        subFilter.length = 1;
        /* Set the options for the relevant cascading dropdown */
        for (let subfilter in filterObject[this.value]) {
            subFilter.options[subFilter.options.length] = new Option(filterObject[this.value][subfilter], subfilter);
        }
    }
};


/* Function to change the current window link, depending on sorting dropdown selection */
function changeSort(val) {
    if (val === 'nr') {
        window.location = '?sort=nr';
    }
    else if (val === 'name') {
        window.location = '?sort=name';
    }
    else if (val === 'pieces') {
        window.location = '?sort=pieces';
    }
    else if (val === 'status') {
        window.location = '?sort=status';
    }
    else if (val === 'loc') {
        window.location = '?sort=loc';
    }
    else if (val === 'missing') {
        window.location = '?sort=missing';
    }
    else if (val === 'fav') {
        window.location = '?sort=fav';
    }
}


/* Function to change the current window link to reverse sorting */
function reverseSort() {
    const url_sort = window.location.search.split('=')[1];
    const current = window.location.origin;

    if (url_sort === 'nr') {
        window.history.pushState("", "", current + '/collections/?rsort=nr');
        window.location.reload();
    }
    else if (url_sort === 'name') {
        window.history.pushState("", "", current + '/collections/?rsort=name');
        window.location.reload();
    }
    else if (url_sort === 'pieces') {
        window.history.pushState("", "", current + '/collections/?rsort=pieces');
        window.location.reload();
    }
    else if (url_sort === 'status') {
        window.history.pushState("", "", current + '/collections/?rsort=status');
        window.location.reload();
    }
    else if (url_sort === 'loc') {
        window.history.pushState("", "", current + '/collections/?rsort=loc');
        window.location.reload();
    }
    else if (url_sort === 'missing') {
        window.history.pushState("", "", current + '/collections/?rsort=missing');
        window.location.reload();
    }
    else if (url_sort === 'fav') {
        window.history.pushState("", "", current + '/collections/?rsort=fav');
        window.location.reload();
    }
}


/* Function to change the current window link, depending on filter dropdown selections */
function changeFilter(val) {
    let filter = document.getElementById('set-filter').value;
    if (filter === '# Pieces') {
        if (val === '0') {
            window.location = '?filter=u500';
        }
        else if (val === '1') {
            window.location = '?filter=u1000';
        }
        else if (val === '2') {
            window.location = '?filter=o500';
        }
        else if (val === '3') {
            window.location = '?filter=o1000';
        }
        else if (val === '4') {
            window.location = '?filter=o2500';
        }
        else if (val === '5') {
            window.location = '?filter=o5000';
        }
    }
    else if (filter === 'Build Status') {
        if (val === '0') {
            window.location = '?filter=bnext';
        }
        else if (val === '1') {
            window.location = '?filter=new';
        }
        else if (val === '2') {
            window.location = '?filter=stored';
        }
        else if (val === '3') {
            window.location = '?filter=wishlist';
        }
    }
    else if (filter === 'Missing Pieces') {
        if (val === '0') {
            window.location = '?filter=miss-yes';
        }
        else if (val === '1') {
            window.location = '?filter=miss-no';
        }
    }
    else if (filter === 'Favourite') {
        if (val === '0') {
            window.location = '?filter=fav-yes';
        }
        else if (val === '1') {
            window.location = '?filter=fav-no';
        }
    }
}


/* Function to toggle the table column selection checkboxes onclick */
window.onload = function() {
    // Create necessary variables
    let divCheckboxes = document.querySelector('#multiselect');
    let checkboxes = document.getElementById("col-toggle-checkboxes");
    let toggleCol = false;
    // Get click events
    document.body.addEventListener('click', function (e) {
        // If clicks are completely outside of the multiselect div, hide the checkboxes
        if (!(divCheckboxes.contains(e.target))) {
            checkboxes.style.display = 'none';
            toggleCol = false;
        }
        // If the checkboxes are expanded and the user clicks the top menu, hide the checkboxes
        else if (toggleCol && e.target.id === 'select-col-default') {
            checkboxes.style.display = 'none';
            toggleCol = false;
        }
        // If the user clicks inside the multiselect div while it's closed, show the checkboxes
        else {
            checkboxes.style.display = 'block';
            toggleCol = true;
        }
    });
}


/* If the user's screen is less than 1300px, insert form for user to select table columns */
if (window.innerWidth <= 1300) {
    document.getElementById('mini-table-toggle').innerHTML = `<form>
                                                                        <div id="multiselect">
                                                                            <div class="select-col-box">
                                                                                <select id="select-col-default">
                                                                                    <option selected hidden>Select Columns</option>
                                                                                </select>
                                                                            </div>
                                                                            <div id="col-toggle-checkboxes">
                                                                                <label for="pic-col">
                                                                                <input type="checkbox" id="pic-col" />Set Image</label>
                                                                                <label for="nr-col">
                                                                                <input type="checkbox" id="nr-col" />Set Number</label>
                                                                                <label for="pieces-col">
                                                                                <input type="checkbox" id="pieces-col" /># Pieces</label>
                                                                                <label for="status-col">
                                                                                <input type="checkbox" id="status-col" />Build Status</label>
                                                                                <label for="loc-col">
                                                                                <input type="checkbox" id="loc-col" />Set Location</label>
                                                                                <label for="miss-col">
                                                                                <input type="checkbox" id="miss-col" />Missing Pieces</label>
                                                                                <label for="fave-col">
                                                                                <input type="checkbox" id="fave-col" />Favourite</label>
                                                                            </div>
                                                                        </div>
                                                                    </form>`
}