from django.shortcuts import render



def ppa_page(request):


    data = {
        'df_years': [
        2023,
        2024,
        2025,
        2026,
        2027,
        2028,
        2029,
        2030,
        2031,
        2032
        ],
        'df_sp': [
        7.297898,
        7.145565,
        6.87408,
        6.509235,
        6.087223,
        5.648306,
        5.229891,
        4.860747,
        4.557713,
        4.325401
        ], 
        'df_pap':[
        6.268739,
        6.171669,
        6.003125,
        5.778582,
        5.519756,
        5.250803,
        4.994169,
        4.767114,
        4.579741,
        4.434819
        ],
        'df_ybl':[
        8.479278,
        8.17815,
        7.6252,
        6.875057,
        6.004353,
        5.098315,
        4.236096,
        3.478531,
        2.861165,
        2.39364
        ],
        'df_hourly_prices_label': [
        "50-100",
        "0-50",
        "150-200",
        "200-250",
        "100-150",
        "250-300",
        "300-350",
        "350-400",
        "400-450",
        "450-500",
        "500-550",
        "550-600",
        "600-650",
        "650-700"
        ],
        'df_hourly_prices': [
        18448,
        18420,
        2176,
        2143,
        1503,
        740,
        209,
        112,
        48,
        18,
        11,
        6,
        5,
        4
        ],
        'npv_values': {
        "Solar Profile": {
            "value": 41.44,
            "color": "rgba(255, 159, 64, 1)"
        },
        "Yearly Baseload": {
            "value": 41.17,
            "color": "rgba(98, 98, 98, 1)"
        },
        "Pay-as-produced": {
            "value": 37.5,
            "color": "rgba(75, 192, 192, 1)"
        }
        },
        'df_hourly_price_year':{
        "hour": {
            "0": 0,
            "11": 1,
            "17": 2,
            "18": 3,
            "19": 4,
            "20": 5,
            "21": 6,
            "22": 7,
            "23": 8,
            "1": 9,
            "2": 10,
            "3": 11,
            "4": 12,
            "5": 13,
            "6": 14,
            "7": 15,
            "8": 16,
            "9": 17,
            "10": 18,
            "12": 19,
            "13": 20,
            "14": 21,
            "15": 22,
            "16": 23
        },
        "min": {
            "0": 0.51,
            "11": 0.51,
            "17": 0.16,
            "18": 0.1,
            "19": 0.03,
            "20": 0.1,
            "21": 0.16,
            "22": 0.16,
            "23": 0.16,
            "1": 1.0,
            "2": 1.49,
            "3": 0.44,
            "4": 0.16,
            "5": 0.16,
            "6": 0.03,
            "7": 0.01,
            "8": 0.01,
            "9": 0.15,
            "10": 1.95,
            "12": 1.95,
            "13": 1.96,
            "14": 1.96,
            "15": 1.95,
            "16": 1.95
        },
        "max": {
            "0": 510.26,
            "11": 450.01,
            "17": 449.5,
            "18": 424.88,
            "19": 429.89,
            "20": 449.6,
            "21": 550.0,
            "22": 600.0,
            "23": 645.0,
            "1": 601.0,
            "2": 582.0,
            "3": 548.09,
            "4": 515.4,
            "5": 460.0,
            "6": 449.9,
            "7": 449.6,
            "8": 514.31,
            "9": 603.08,
            "10": 651.0,
            "12": 700.0,
            "13": 654.91,
            "14": 651.0,
            "15": 650.0,
            "16": 600.0
        },
        "mean": {
            "0": 73.99748221127523,
            "11": 69.0983360700603,
            "17": 65.86733442802402,
            "18": 63.738921729611334,
            "19": 63.015216201423094,
            "20": 65.02551724137926,
            "21": 70.3660645867542,
            "22": 76.46460317460318,
            "23": 79.05784345922278,
            "1": 79.09243021346471,
            "2": 76.7595621237,
            "3": 74.24858237547896,
            "4": 73.24149972632736,
            "5": 72.17403940886706,
            "6": 70.027531472359,
            "7": 67.90413245758077,
            "8": 68.53936507936513,
            "9": 72.64446633825946,
            "10": 77.79344280240835,
            "12": 82.67279693486586,
            "13": 85.34997263273127,
            "14": 84.76304871373841,
            "15": 80.6503995621237,
            "16": 75.44131174533491
        }
        },
    }

    return render(request,'ppa/ppa_chart.html',data)