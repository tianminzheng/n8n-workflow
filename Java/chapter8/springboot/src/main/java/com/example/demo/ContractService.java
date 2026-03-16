package com.example.demo;

import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

@Service
public class ContractService {

    private final Map<String, Contract> contractMap;

    public ContractService() {
        this.contractMap = new HashMap<>();
        initializeContracts();
    }

    private void initializeContracts() {
        contractMap.put("CON-2024-001", new Contract(
                "CON-2024-001",
                "CT-2024-001",
                new BigDecimal("10000.00"),
                LocalDate.of(2024, 1, 1),
                LocalDate.of(2024, 12, 31),
                "供应商A",
                "30天",
                "active"
        ));

        contractMap.put("CON-2024-002", new Contract(
                "CON-2024-002",
                "CT-2024-002",
                new BigDecimal("25000.00"),
                LocalDate.of(2024, 1, 1),
                LocalDate.of(2024, 12, 31),
                "供应商B",
                "60天",
                "active"
        ));

        contractMap.put("CON-2024-003", new Contract(
                "CON-2024-003",
                "CT-2024-003",
                new BigDecimal("50000.00"),
                LocalDate.of(2024, 1, 1),
                LocalDate.of(2024, 12, 31),
                "供应商A",
                "30天",
                "active"
        ));

        contractMap.put("CON-2024-004", new Contract(
                "CON-2024-004",
                "CT-2024-004",
                new BigDecimal("30000.00"),
                LocalDate.of(2024, 1, 1),
                LocalDate.of(2024, 12, 31),
                "供应商D",
                "45天",
                "active"
        ));
    }

    public Contract getContractById(String contractId) {
        return contractMap.get(contractId);
    }
}