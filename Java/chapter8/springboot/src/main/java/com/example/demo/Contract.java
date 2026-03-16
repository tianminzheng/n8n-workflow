package com.example.demo;


import java.math.BigDecimal;
import java.time.LocalDate;

public class Contract {
    private String contractId;
    private String contractNumber;
    private BigDecimal amount;
    private LocalDate startDate;
    private LocalDate endDate;
    private String supplier;
    private String paymentTerms;
    private String status;

    public Contract() {}

    public Contract(String contractId, String contractNumber, BigDecimal amount,
                    LocalDate startDate, LocalDate endDate, String supplier,
                    String paymentTerms, String status) {
        this.contractId = contractId;
        this.contractNumber = contractNumber;
        this.amount = amount;
        this.startDate = startDate;
        this.endDate = endDate;
        this.supplier = supplier;
        this.paymentTerms = paymentTerms;
        this.status = status;
    }

    // Getters and Setters
    public String getContractId() { return contractId; }
    public void setContractId(String contractId) { this.contractId = contractId; }

    public String getContractNumber() { return contractNumber; }
    public void setContractNumber(String contractNumber) { this.contractNumber = contractNumber; }

    public BigDecimal getAmount() { return amount; }
    public void setAmount(BigDecimal amount) { this.amount = amount; }

    public LocalDate getStartDate() { return startDate; }
    public void setStartDate(LocalDate startDate) { this.startDate = startDate; }

    public LocalDate getEndDate() { return endDate; }
    public void setEndDate(LocalDate endDate) { this.endDate = endDate; }

    public String getSupplier() { return supplier; }
    public void setSupplier(String supplier) { this.supplier = supplier; }

    public String getPaymentTerms() { return paymentTerms; }
    public void setPaymentTerms(String paymentTerms) { this.paymentTerms = paymentTerms; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}