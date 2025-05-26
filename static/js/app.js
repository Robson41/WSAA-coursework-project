document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("itemForm");
  const itemList = document.getElementById("itemList");
  const nameInput = document.getElementById("name");
  const descriptionInput = document.getElementById("description");
  let editItemId = null;

  async function fetchItems() {
    try {
      const response = await fetch("/api/items");
      if (!response.ok) throw new Error("Failed to fetch items");
      const items = await response.json();
      renderItems(items);
    } catch (err) {
      console.error("Error fetching items:", err);
    }
  }

  function renderItems(items) {
    itemList.innerHTML = "";
    items.forEach(item => {
      const li = document.createElement("li");
      li.textContent = `${item.name} - ${item.description}`;
      li.dataset.id = item._id;

      const editBtn = document.createElement("button");
      editBtn.textContent = "Edit";
      editBtn.addEventListener("click", () => loadItemForEdit(item._id));

      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Delete";
      deleteBtn.addEventListener("click", () => deleteItem(item._id));

      li.appendChild(editBtn);
      li.appendChild(deleteBtn);
      itemList.appendChild(li);
    });
  }

  async function loadItemForEdit(id) {
    try {
      const response = await fetch(`/api/items/${id}`);
      if (!response.ok) throw new Error("Item not found");
      const item = await response.json();
      nameInput.value = item.name;
      descriptionInput.value = item.description;
      editItemId = id;
    } catch (err) {
      console.error("Error loading item for edit:", err);
    }
  }

  async function deleteItem(id) {
    try {
      const response = await fetch(`/api/items/${id}`, { method: "DELETE" });
      if (!response.ok) throw new Error("Failed to delete item");
      fetchItems();
    } catch (err) {
      console.error("Error deleting item:", err);
    }
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = nameInput.value.trim();
    const description = descriptionInput.value.trim();

    if (!name) {
      alert("Name is required");
      return;
    }

    try {
      let response;
      if (editItemId) {
        response = await fetch(`/api/items/${editItemId}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, description }),
        });
      } else {
        response = await fetch("/api/items", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, description }),
        });
      }
      if (!response.ok) throw new Error("Failed to save item");
      nameInput.value = "";
      descriptionInput.value = "";
      editItemId = null;
      fetchItems();
    } catch (err) {
      console.error("Error saving item:", err);
    }
  });

  fetchItems();
});
