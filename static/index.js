const addItem = async e => {
	e.preventDefault();

	const form = e.target;
	const data = {
		name: form.name.value,
		price: form.price.value,
		provider: form.provider.value,
		frequency: form.frequency.value
	};

	const response = await fetch("/add", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(data)
	});

	const result = await response.json();

	if (result.status !== "ok") {
		console.error("bug");
	}
	const table = document.getElementById("itemsTable").querySelector("tbody");
	const row = document.createElement("tr");
	row.setAttribute(
		"data-index",
		document.querySelectorAll("#itemsTable tbody tr").length
	);

	row.innerHTML = `
                <td>${result.item.name}</td>
                <td>${result.item.price}</td>
                <td>${result.item.provider}</td>
                <td>${result.item.frequency}</td>
                <td>
                    <button class="btn btn-danger btn-sm delete-btn">Delete</button>
                </td>
            `;

	table.appendChild(row);

	row.querySelector(".delete-btn").addEventListener("click", deleteItem);
	const modalElement = document.getElementById("addModal");
	const modal = bootstrap.Modal.getInstance(modalElement);
	modal.hide();

	form.reset();
};

const deleteItem = async e => {
	const row = e.target.closest("tr");
	const index = row.getAttribute("data-index");

	const response = await fetch(`/delete/${index}`, {
		method: "DELETE"
	});

	const result = await response.json();

	if (result.status === "ok") {
		row.remove();
	}
};

document.getElementById("addForm").addEventListener("submit", addItem);

document.querySelectorAll(".delete-btn").forEach(btn => {
	btn.addEventListener("click", deleteItem);
});
