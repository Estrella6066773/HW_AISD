package io.camunda.demo.hospital.domain;

/**
 * Status values for {@link PaymentLedger}.
 * {@code INVESTIGATE} means charge may already have happened — do not auto-charge again.
 */
public enum PaymentLedgerStatus {
	SUCCESSFUL,
	UNSUCCESSFUL,
	INVESTIGATE
}
