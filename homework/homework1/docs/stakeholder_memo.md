# Stakeholder Memo – Inventory Forecasting for Perishable Goods

## Project Overview
Our grocery chain currently experiences frequent stockouts and overstocking for perishable goods such as fresh produce, dairy, and bakery items. Stockouts lead to lost sales and customer dissatisfaction, while overstocking drives waste, spoilage, and profit loss. Ordering is mostly driven by store manager intuition and static rules, which cannot adapt to local demand variability, promotional events, or weather impacts.

We aim to implement a **data-driven demand forecasting system** for high-turnover, perishable SKUs. By generating accurate, daily forecasts per store, we can reduce waste, improve product availability, and boost revenue.

---

## Stakeholders & Users
**Decision-makers:**
- Supply Chain Director
- Category Managers

**Primary Users:**
- Store Managers
- Replenishment Planners

**Workflow Context:**
Forecasts will be generated overnight and integrated into the store ordering system by 6 AM daily, covering a 1–14 day forecast horizon.

---

## Project Goals
- **Primary Goal:** Reduce waste and stockouts through improved demand forecasting.
- **Secondary Goals:** Improve customer satisfaction, enhance supply chain efficiency, and reduce manual forecasting effort.

---

## Useful Outputs
**Type:** Predictive (time-series / regression-based)  
**Artifact:** Automated forecasting pipeline producing daily demand forecasts per SKU-store combination  
**Metrics:**
- Forecast accuracy (MAPE)
- Waste reduction (%)
- Sales uplift from reduced stockouts

---

## Assumptions & Constraints
- At least 2 years of historical daily sales data available
- Access to promotions, pricing history, and weather data
- Batch forecast generation allowed (<3 hours runtime)
- Must comply with company data governance policies
- Perishable SKUs require forecast horizons under 14 days

---

## Risks & Unknowns
- Demand spikes from local events or competitor actions
- Supplier delivery delays impacting inventory even with accurate forecasts
- Data sparsity for new or seasonal SKUs
- Integration challenges with the existing ordering system
- Model drift due to changing customer behavior

---

## Lifecycle Mapping
- **Goal A:** Reduce waste & stockouts → Stage 01 → Problem definition document
- **Goal B:** Build forecasting prototype → Stage 02 → MVP forecast model tested on historical data
- **Goal C:** Integrate into ordering workflow → Stage 03 → Productionized forecasting pipeline with dashboard monitoring
