$(document).ready(function() {
    var deviceList = $('#device-list');

    function loadDevices() {
        if (deviceList.length) {
            $.ajax({
                url: 'http://localhost:5050/device',
                method: 'GET',
                success: function(response) {
                    var devices = response.devices;
                    deviceList.empty(); // Clear any existing content

                    // Create table structure
                    var table = $('<table></table>').addClass('device-table');
                    var thead = $('<thead></thead>');
                    var tbody = $('<tbody></tbody>');

                    // Add table headers
                    thead.append('<tr><th>ID</th><th>Name</th><th>Location</th></tr>');
                    table.append(thead);

                    // Add table rows
                    devices.forEach(function(device) {
                        var row = $('<tr></tr>');
                        row.append($('<td></td>').text(device.id));
                        row.append($('<td></td>').text(device.name));
                        row.append($('<td></td>').text(device.location));
                        tbody.append(row);
                    });

                    table.append(tbody);
                    deviceList.append(table);
                },
                error: function(error) {
                    console.error('Error fetching devices:', error);
                }
            });
        }
    }

    // Load devices on page load
    loadDevices();

    // Modal handling
    var modal = $('#device-modal');
    var btn = $('#add-device-button');
    var span = $('.close');

    btn.on('click', function() {
        modal.show();
    });

    span.on('click', function() {
        modal.hide();
    });

    $(window).on('click', function(event) {
        if (event.target == modal[0]) {
            modal.hide();
        }
    });

    // Form submission
    $('#device-form').on('submit', function(event) {
        event.preventDefault();
        var formData = {
            id: $('#device-id').val(),
            name: $('#device-name').val(),
            location: $('#device-location').val()
        };

        $.ajax({
            url: 'http://localhost:5050/device',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                modal.hide();
                loadDevices(); // Refresh the device list
            },
            error: function(error) {
                console.error('Error adding device:', error);
            }
        });
    });
});