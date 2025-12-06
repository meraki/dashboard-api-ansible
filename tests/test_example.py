"""
Example test file showing how to write custom tests for specific queries.

This file demonstrates how to write focused tests for individual queries
or specific validation scenarios.
"""
import jq
import json
import pytest


class TestExampleQueries:
    """Example test class showing custom test patterns."""

    def test_specific_query_output_format(self, query_data, load_fixture):
        """Example: Test a specific query's output format."""
        module_fqcn = "cisco.meraki.devices_info"
        fixture_data = load_fixture(module_fqcn)

        if fixture_data is None:
            pytest.skip(f"Fixture file not found for {module_fqcn}")

        final_response = {"meraki_response": fixture_data}
        jq_query = query_data[module_fqcn]["query"]

        compiled_query = jq.compile(jq_query)
        results = compiled_query.input(final_response).all()

        # Custom assertions
        assert len(results) > 0, "Should return at least one device"
        assert all("serial" in str(item) for item in results), "All items should reference serial"

    def test_empty_response_handling(self, query_data):
        """Example: Test that queries handle empty/null responses correctly."""
        module_fqcn = "cisco.meraki.devices_info"

        if module_fqcn not in query_data:
            pytest.skip(f"Query not found for {module_fqcn}")

        jq_query = query_data[module_fqcn]["query"]

        # Test with null response
        null_response = {"meraki_response": None}
        compiled_query = jq.compile(jq_query)
        results = compiled_query.input(null_response).all()

        assert isinstance(results, list), "Should return a list even for null input"
        assert len(results) == 0, "Should return empty list for null input"

        # Test with empty object
        empty_response = {"meraki_response": {}}
        results = compiled_query.input(empty_response).all()
        assert isinstance(results, list), "Should return a list even for empty input"

    def test_query_performance(self, query_data, load_fixture):
        """Example: Test query execution time (if needed)."""
        import time

        module_fqcn = "cisco.meraki.devices_info"
        fixture_data = load_fixture(module_fqcn)

        if fixture_data is None:
            pytest.skip(f"Fixture file not found for {module_fqcn}")

        final_response = {"meraki_response": fixture_data}
        jq_query = query_data[module_fqcn]["query"]

        compiled_query = jq.compile(jq_query)

        # Measure execution time
        start_time = time.time()
        results = compiled_query.input(final_response).all()
        execution_time = time.time() - start_time

        # Assert reasonable performance (adjust threshold as needed)
        assert execution_time < 1.0, f"Query took {execution_time:.3f}s, should be < 1.0s"

        # Verify results are still valid
        assert isinstance(results, list), "Results should be a list"

