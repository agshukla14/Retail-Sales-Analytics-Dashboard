const fs = require('fs');

console.log("=== RUNNING DASHBOARD TESTS ===");

// 1. Check data.js
let dataContent = fs.readFileSync('data.js', 'utf8');
dataContent = dataContent.replace(/\/\/[^\n]*/g, '');
const jsonStr = dataContent.replace(/const\s+RAW_SALES_DATA\s*=\s*/, '').replace(/;\s*$/, '');
const rawData = JSON.parse(jsonStr);

console.log(`[Test 1] Loaded RAW_SALES_DATA: ${rawData.length} records.`);
if (rawData.length !== 500) {
  throw new Error(`Expected 500 records, got ${rawData.length}`);
}

// 2. Test mathematical accuracy against Golden Truth
let totalRevenue = 0;
let totalQuantity = 0;
const uniqueCustomers = new Set();
const uniqueOrders = new Set();
const categories = {};
const regions = {};
const genders = {};

rawData.forEach(r => {
  const p = parseFloat(r.Price);
  const q = parseInt(r.Quantity, 10);
  const rev = p * q;
  totalRevenue += rev;
  totalQuantity += q;
  uniqueCustomers.add(r.Customer_ID);
  uniqueOrders.add(r.Order_ID);

  categories[r.Product_Category] = (categories[r.Product_Category] || 0) + rev;
  regions[r.Region] = (regions[r.Region] || 0) + rev;
  genders[r.Gender] = (genders[r.Gender] || 0) + rev;
});

console.log(`[Test 2] Total Revenue: $${totalRevenue.toFixed(2)} (Expected: $827588.10)`);
console.log(`[Test 2] Total Orders: ${uniqueOrders.size} (Expected: 500)`);
console.log(`[Test 2] Total Quantity: ${totalQuantity} (Expected: 1527)`);
console.log(`[Test 2] Unique Customers: ${uniqueCustomers.size} (Expected: 99)`);

if (Math.abs(totalRevenue - 827588.10) > 0.05) throw new Error("Revenue mismatch!");
if (uniqueOrders.size !== 500) throw new Error("Orders count mismatch!");
if (totalQuantity !== 1527) throw new Error("Quantity mismatch!");
if (uniqueCustomers.size !== 99) throw new Error("Unique customers mismatch!");

// 3. Test filtering logic
console.log("\n[Test 3] Testing Filter Combinations:");

// Filter: Electronics only
const elecRows = rawData.filter(r => r.Product_Category === 'Electronics');
const elecRev = elecRows.reduce((sum, r) => sum + r.Price * r.Quantity, 0);
console.log(`- Electronics Only: ${elecRows.length} orders, Revenue: $${elecRev.toFixed(2)} (Expected: $474295.34)`);
if (Math.abs(elecRev - 474295.34) > 0.05) throw new Error("Electronics revenue mismatch!");

// Filter: West Region only
const westRows = rawData.filter(r => r.Region === 'West');
const westRev = westRows.reduce((sum, r) => sum + r.Price * r.Quantity, 0);
console.log(`- West Region Only: ${westRows.length} orders, Revenue: $${westRev.toFixed(2)} (Expected: $226685.88)`);
if (Math.abs(westRev - 226685.88) > 0.05) throw new Error("West revenue mismatch!");

// Filter: Female Only
const femaleRows = rawData.filter(r => r.Gender === 'Female');
const femaleRev = femaleRows.reduce((sum, r) => sum + r.Price * r.Quantity, 0);
console.log(`- Female Only: ${femaleRows.length} orders, Revenue: $${femaleRev.toFixed(2)} (Expected: $382291.09)`);
if (Math.abs(femaleRev - 382291.09) > 0.05) throw new Error("Female revenue mismatch!");

// Filter: Date Range Q1 (2023-01-01 to 2023-03-31)
const q1Rows = rawData.filter(r => r.Order_Date >= '2023-01-01' && r.Order_Date <= '2023-03-31');
const q1Rev = q1Rows.reduce((sum, r) => sum + r.Price * r.Quantity, 0);
console.log(`- Q1 Date Filter: ${q1Rows.length} orders, Revenue: $${q1Rev.toFixed(2)} (Expected: $177248.82)`);
if (Math.abs(q1Rev - 177248.82) > 0.05) throw new Error("Q1 revenue mismatch!");

// 4. Test Top 10 Orders Sort
const sortedOrders = [...rawData].sort((a, b) => (b.Price * b.Quantity) - (a.Price * a.Quantity));
console.log(`\n[Test 4] Top Order ID: #${sortedOrders[0].Order_ID} with Revenue $${(sortedOrders[0].Price * sortedOrders[0].Quantity).toFixed(2)} (Expected: #378, $9881.65)`);
if (sortedOrders[0].Order_ID !== 378) throw new Error("Top order mismatch!");

console.log("\n>>> ALL TESTS PASSED SUCCESSFULLY! <<<");
