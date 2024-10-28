**Business Requirement Document (BRD)** Travel Loan  
_Credit and Product Management_  
_Private & Confidential_

### Document Revision History

|Version|Date|Description|Author|Reviewer|
|---|---|---|---|---|
|1.0|9 Sep 2024|Draft BRD|[Your Name]|[Reviewer’s Name]|

---

### 1. Background

The travel loan is designed to support customers requiring financial assistance for travel-related expenses, including personal, corporate, and student trips. The product aims to serve a range of travel purposes, such as business, education, and tourism, while providing tailored loan structures to enhance convenience and financial accessibility.

---

### 2. Project Objective

- **Customer Support**: Provide a financing solution that addresses customers’ travel needs by covering expenses such as accommodations, transportation, and other travel-related costs.
- **Competitive Positioning**: Establish the bank as a leading provider of unique, customer-focused loan products.
- **Profitability**: Ensure the loan product is profitable by managing potential risks and offering a viable interest rate structure.
- **Customer Retention**: Increase customer loyalty and retention by offering value-added services for frequent travelers.

---

### 3. Target Release Feature

**Travel Loan Product**

|Milestone|Date|
|---|---|
|Development Start|[Start Date]|
|UAT Start|[UAT Date]|
|Change Start|[Change Date]|
|Release Date|[Release Date]|

---

### 4. Business Requirement

**Private & Confidential**

#### Features & Descriptions

- **Account Opening Process**:
    - The loan account will be created based on the customer's travel financing needs, requiring an upfront deposit of interest into a CASA account.
    - Once approved, funds are transferred from the loan settlement GL to the customer’s CASA account, with interest deducted for the entire loan tenor in advance.
    - Loan funds will be blocked in the CASA account and released upon completion of the loan term.

|Account Class|Minimum Loan Amount|Maximum Loan Amount|Interest Rate|Interest Payment|
|---|---|---|---|---|
|Travel Loan|5,000 USD|5 Million MMK|10-12% p.a.|Deducted upfront|

---

### 5. Stakeholders

- **Branch Operations**
- **Travel Loan BU**
- **Core Banking Team**
- **Finance Department**
- **Legal & Compliance**
- **Marketing Department**
- **Learning & Development Team**

---

### 6. Account Classes and GL Code

**Private & Confidential**

- **Tenor**: 1-12 months
- **Interest Calculation**: Daily Accrued
- **Disbursement**: Loan amount disbursed to customer’s CASA account via Loan Settlement GL.

| Required Documents | Visa Application | Education Application |
| ------------------ | ---------------- | --------------------- |
| - Loan Application | X                | X                     |
| - Proof of Travel  | X                |                       |
| - Admission Letter |                  | X                     |
| - Source of Income | X                | X                     |
| - Promissory Note  | X                | X                     |

**Eligibility**: Applicants aged 21 and above. Parents may apply on behalf of children if they meet eligibility requirements.

**Repayment**: Blocked funds are released on the due date, and the process is automated.

**Fees and Charges**: Processing fee - 1% of the loan amount.

---

### 7. Requirement Specification Sign-Off

|Role|Signature|Date|
|---|---|---|
|Project Owner||[Date]|
|Product Manager||[Date]|
|Reviewer||[Date]|

---

This format aligns with the financing BRD style, focusing on travel-related needs and structured details. Let me know if you'd like further adjustments!