async function fetchBreweries(query) {
  const params = new URLSearchParams(query).toString();
  const r = await fetch(`/api/breweries?${params}`);
  if (!r.ok) throw new Error("API error");
  return await r.json();
}

function renderRows(list) {
  const tbody = document.querySelector("#results tbody");
  tbody.innerHTML = "";
  list.forEach(b => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${b.name}</td>
      <td>${b.brewery_type}</td>
      <td>${b.city}</td>
      <td>${b.state}</td>
      <td>${b.website_url ? `<a href="${b.website_url}" target="_blank">link</a>` : ""}</td>`;
    tbody.appendChild(tr);
  });
}

document.getElementById("searchForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = Object.fromEntries(new FormData(e.target));
  try {
    const data = await fetchBreweries(formData);
    renderRows(data);
  } catch (err) {
    alert(err.message);
  }
});
