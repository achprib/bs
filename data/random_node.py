# 随机生成节点坐标及数据生产速率和能量消耗速率
import pandas as pd
import numpy as np
import os
# 导入刚才定义的配置参数
from config import AREA_WIDTH, AREA_HEIGHT, NODE_COUNT, R_I_RANGE, P_I_RANGE, NODES_CSV

def generate_nodes():

    # 设置随机种子保证实验可重复
    np.random.seed(42)

    # 1. 随机生成坐标 (x, y) - 使用 config 中的范围
    x_coords = np.random.uniform(0, AREA_WIDTH, NODE_COUNT)
    y_coords = np.random.uniform(0, AREA_HEIGHT, NODE_COUNT)

    # 2. 生成数据产生速率 R_i (Kbps)
    data_rates = np.random.uniform(R_I_RANGE[0], R_I_RANGE[1], NODE_COUNT)

    # 3. 生成能量消耗率 P_i (J/sec)
    energy_consumption = np.random.uniform(P_I_RANGE[0], P_I_RANGE[1], NODE_COUNT)

    # 构建 DataFrame
    df = pd.DataFrame({
        'node_id': range(1, NODE_COUNT + 1),
        'x': np.round(x_coords, 2),
        'y': np.round(y_coords, 2),
        'data_rate_kbps': np.round(data_rates, 2),
        'energy_cons_jps': np.round(energy_consumption, 3)
    })

    # 保存到 config 中指定的路径
    df.to_csv(NODES_CSV, index=False)
    print(f"成功根据 config 参数生成 {NODE_COUNT} 个节点，并保存至: {NODES_CSV}")

if __name__ == "__main__":
    generate_nodes()