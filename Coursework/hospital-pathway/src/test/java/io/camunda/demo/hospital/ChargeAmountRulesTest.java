package io.camunda.demo.hospital;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.Test;

class ChargeAmountRulesTest {

	@Test
	void acceptsTwoDecimalAmountsInsideRange() {
		assertThat(ChargeAmountRules.require("10.01")).isEqualTo("10.01");
		assertThat(ChargeAmountRules.require("10.00")).isEqualTo("10.00");
		assertThat(ChargeAmountRules.require(" 99999.99 ")).isEqualTo("99999.99");
	}

	@Test
	void rejectsBlankLettersNegativeAndWrongScale() {
		assertThatThrownBy(() -> ChargeAmountRules.require(null)).hasMessageContaining("required");
		assertThatThrownBy(() -> ChargeAmountRules.require("")).hasMessageContaining("required");
		assertThatThrownBy(() -> ChargeAmountRules.require("abc")).hasMessageContaining("precision");
		assertThatThrownBy(() -> ChargeAmountRules.require("-1.00")).hasMessageContaining("precision");
		assertThatThrownBy(() -> ChargeAmountRules.require("10")).hasMessageContaining("precision");
		assertThatThrownBy(() -> ChargeAmountRules.require("10.1")).hasMessageContaining("precision");
		assertThatThrownBy(() -> ChargeAmountRules.require("10.001")).hasMessageContaining("precision");
		assertThatThrownBy(() -> ChargeAmountRules.require("0.00")).hasMessageContaining("range");
		assertThatThrownBy(() -> ChargeAmountRules.require("100000.00")).hasMessageContaining("range");
	}
}
