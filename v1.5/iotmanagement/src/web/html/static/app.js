$(document).ready(function() {
    var deviceList = $('#device-list');
    var modal = $('#device-modal');
    var detailsModal = $('#device-details-modal');
    var btn = $('#add-device-button');
    var span = $('.close');
    var spanDetails = $('.close-details');

    function createTable(devices) {
        var table = $('<table></table>').addClass('device-table');
        var thead = $('<thead></thead>');
        var tbody = $('<tbody></tbody>');

        // Add table headers
        thead.append('<tr><th>ID</th><th>Name</th><th>Location</th><th>Actions</th></tr>');
        table.append(thead);

        // Add table rows
        devices.forEach(function(device) {
            var row = $('<tr></tr>');
            row.append($('<td></td>').text(device.id));
            row.append($('<td></td>').text(device.name));
            row.append($('<td></td>').text(device.location));
            var deleteButton = $('<button>Delete</button>').on('click', function() {
                deleteDevice(device.id);
            });
            var viewButton = $('<button>View</button>').on('click', function() {
                viewDeviceDetails(device.id);
            });
            row.append($('<td></td>').append(viewButton).append(deleteButton));
            tbody.append(row);
        });

        table.append(tbody);
        return table;
    }

    function loadDevices() {
        if (deviceList.length) {
            $.ajax({
                url: 'http://localhost:5055/device',
                method: 'GET',
                success: function(response) {
                    var devices = response.devices;
                    deviceList.empty(); // Clear any existing content
                    var table = createTable(devices);
                    deviceList.append(table);
                },
                error: function(error) {
                    console.error('Error fetching devices:', error);
                }
            });
        }
    }

    function showModal() {
        modal.show();
    }

    function hideModal() {
        modal.hide();
    }

    function showDetailsModal() {
        detailsModal.show();
    }

    function hideDetailsModal() {
        detailsModal.hide();
    }

    function handleFormSubmit(event) {
        event.preventDefault();
        var formData = {
            id: $('#device-id').val(),
            name: $('#device-name').val(),
            location: $('#device-location').val()
        };

        $.ajax({
            url: 'http://localhost:5055/device',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                hideModal();
                loadDevices(); // Refresh the device list
            },
            error: function(error) {
                console.error('Error adding device:', error);
            }
        });
    }

    function deleteDevice(deviceId) {
        $.ajax({
            url: 'http://localhost:5055/device/' + deviceId,
            method: 'DELETE',
            success: function(response) {
                loadDevices(); // Refresh the device list
            },
            error: function(error) {
                console.error('Error deleting device:', error);
            }
        });
    }

    function viewDeviceDetails(deviceId) {
        $.ajax({
            url: 'http://localhost:5055/device/' + deviceId,
            method: 'GET',
            success: function(response) {
                var device = response.device;
                var sensor_data_summary = response.sensor_data_summary;
                $('#details-id').text(device.id);
                $('#details-name').text(device.name);
                $('#details-location').text(device.location);
                if (sensor_data_summary && sensor_data_summary.temperature) {
                    if (sensor_data_summary.temperature.latest_value) {
                        $('#details-temp-latest-value').text(sensor_data_summary.temperature.latest_value);
                    }
                    if (sensor_data_summary.temperature.latest_status) {
                        $('#details-temp-latest-status').text(sensor_data_summary.temperature.latest_status);
                    }
                }
                showDetailsModal();
            },
            error: function(error) {
                console.error('Error fetching device details:', error);
            }
        });
    }

    // Event bindings
    btn.on('click', showModal);
    span.on('click', hideModal);
    spanDetails.on('click', hideDetailsModal);
    $(window).on('click', function(event) {
        if (event.target == modal[0]) {
            hideModal();
        }
        if (event.target == detailsModal[0]) {
            hideDetailsModal();
        }
    });
    $('#device-form').on('submit', handleFormSubmit);

    // Initial load
    loadDevices();
});