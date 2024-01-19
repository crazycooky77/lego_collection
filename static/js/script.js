let filterObject = {
    "# Pieces": ["<500", "<1000", ">500", ">1000", ">2500", ">5000"],
    "Build Status": ["Build Next", "New", "Stored", "Wish List"],
    "Missing Pieces": ["Yes", "No"],
    "Favourite": ["Yes", "No"]
};
window.onload = function() {
    let filterSel = document.getElementById("set-filter");
    let subFilter = document.getElementById("sub-filter");
    for (let filter in filterObject) {
        filterSel.options[filterSel.options.length] = new Option(filter, filter);
    }
    filterSel.onchange = function() {
        subFilter.length = 1;
        for (let subfilter in filterObject[this.value]) {
            subFilter.options[subFilter.options.length] = new Option(filterObject[this.value][subfilter], subfilter);
        }
    }
};


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
