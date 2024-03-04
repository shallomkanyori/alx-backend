/**
 * Simple stock handling express app
 */
import { createClient } from 'redis';
import { promisify } from 'util';
const express = require('express');

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Redis
const client = createClient();
client.get = promisify(client.get);

// Express
const app = express();
const port = 1245;

/**
 * Returns an item from listProducts with the given id
 * @param {number} id The id of the item to get
 * @returns {object | null} The item with the given id or null if no item found
 */
function getItemById (id) {
  return listProducts.find((item) => item.id === id);
}

/**
 * Set reserved stock for an item in Redis
 * @param {number} itemId The id of the item to reserve stock for
 * @param {number} stock The amount of stock to reserve
 */
function reserveStockById (itemId, stock) {
  client.set(itemId, stock);
}

/**
 * Returns the reserved stock for a specific item
 * @param {number} itemId The id of the item to get the reserved stock for
 * @returns {number} The reserved stock of the item
 */
async function getCurrentReservedStockById (itemId) {
  return await client.get(itemId);
}

app.get('/list_products', function (req, res) {
  const data = [];

  for (const item of listProducts) {
    const itemJson = {
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock
    };

    data.push(itemJson);
  }

  res.json(data);
});

app.get('/list_products/:itemId', async function (req, res) {
  const item = getItemById(Number(req.params.itemId));
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currQuantity = await getCurrentReservedStockById(item.id) ?? item.stock;
  const data = {
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currQuantity
  };

  res.json(data);
});

app.get('/reserve_product/:itemId', async function (req, res) {
  const item = getItemById(Number(req.params.itemId));
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currQuantity = await getCurrentReservedStockById(item.id) ?? item.stock;
  if (currQuantity < 1) {
    res.json({ status: 'Not enough stock available', itemId: item.id });
  } else {
    reserveStockById(item.id, currQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId: item.id });
  }
});

app.listen(port, console.log(`Server listening on port ${port}`));
